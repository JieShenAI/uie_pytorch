```
create (d :Doc{name: "测试发展规划"}) return d
```

```
create r = (:Subject{name:"物流"})-[:开展]->(:Object{name:"改革"})
return r
```

```
match (d :Doc{name: "测试发展规划"})
match r = (s:Subject{name:"物流"})-[:开展]->(:Object{name:"改革"})
create l = ((d)-[:link]->(s))
return l
```

查询某个点是否存在
