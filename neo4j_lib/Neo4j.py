import os
from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher
from dotenv import load_dotenv, find_dotenv
from typing import Union
from copy import deepcopy

from .KgUtils import EntityLimit, TripleLimit

load_dotenv(find_dotenv())


class Neo4jLimit:
    """
    连接neo4j数据库，并将三元组自动插入其中
    """

    def __init__(self):
        # self.graph = Graph("http://localhost:7474", username="neo4j", password="pass")
        self.graph = Graph(
            password=os.environ['pwd']
        )
        self.node_matcher = NodeMatcher(self.graph)
        self.relation_matcher = RelationshipMatcher(self.graph)

    def _create_node(self, label, **kwargs):
        node = Node(label, **kwargs)
        self.graph.create(node)
        return node

    def _find_entity(self, ent: EntityLimit) -> Union[None, EntityLimit]:
        label = ent.type
        d = deepcopy(ent.__dict__)
        d.pop("type")
        return NodeMatcher(self.graph).match(label, **d).first()

    def get_node(self, ent: EntityLimit) -> Node:
        """
        根据输入的三元组，若neo4j中已有则查询返回，否则就创建新结点返回
        """
        ent_node = self._find_entity(ent)
        if ent_node:
            return ent_node
        if not self._find_entity(ent):
            label = ent.type
            d = deepcopy(ent.__dict__)
            d.pop("type")
            return self._create_node(label, **d)

    def create_triple(self, triple: TripleLimit):
        """
        根据给定的三元组，创建三元组，若结点和关系在neo4j中已有，则无需重复创建
        """
        subject_node = self.get_node(triple.subject)
        object_node = self.get_node(triple.object)
        # 查询关系是否存在
        relation = self.relation_matcher.match(
            [subject_node, object_node],
            r_type=triple.relation).first()
        if not relation:
            self.graph.create(
                Relationship(subject_node, triple.relation, object_node)
            )


if __name__ == '__main__':
    neo = Neo4jLimit()
