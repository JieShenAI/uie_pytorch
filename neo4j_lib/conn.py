from py2neo import Node, Relationship, Graph, NodeMatcher, Subgraph
from jshen.io import load_yaml

pwd = load_yaml("../.private/pwd.yaml")["pwd"]
graph = Graph(
    # "http://localhost:7474/db/data/demo.db",
    "http://localhost:7474",
    password="jieshenai"
)

print(graph)

# 定义node
# node_1 = Node('英雄', name='张无忌')
# node_2 = Node('英雄', name='杨逍', 武力值='100')
# node_3 = Node('派别', name='明教')
#
# # 存入图数据库
# test_graph.create(node_1)
# test_graph.create(node_2)
# test_graph.create(node_3)
# print(node_1)


node = Node('wd', name='zsf')
graph.create(node)
# graph.commit()

