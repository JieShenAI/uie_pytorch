from py2neo import Node, Relationship, Graph, NodeMatcher

doc = Node('Doc', name='测试发展规划')
# a = Node('Person', name='Alice')
# b = Node('Person', name='Bob')
# r = Relationship(a, 'KNOWS', b)
# s = a | b | r
graph = Graph(
    # "http://localhost:7474/",
    password='jieshenai'
)

print("raw", doc)

data = graph.run("match (d :Doc) return d")
print(type(data))

for item in data:
    print(item)

# neo4j 查询某个节点是否存在

node_matcher = NodeMatcher(graph)  # 节点匹配器
a = node_matcher.match('Doc')  # 提取满足属性值的节点
for item in a:
    print(type(item))
    print(item)
