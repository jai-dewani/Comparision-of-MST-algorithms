from Krushkal import Krushkal
from Prims import Prims

v = 4
edges = [
    [0,1,10],
    [0,2,6],
    [0,3,5],
    [1,3,15],
    [2,3,4]
]

k = Krushkal(v)
for i in edges:
    k.addEdge(i[0],i[1],i[2])
k.KruskalMST() 

p = Prims(v) 
p.graph = [[0 for i in range(v)] for j in range(v)]
for i in edges:
    x = i[0]
    y = i[1]
    w = i[2]
    p.graph[x][y] = w
    p.graph[y][x] = w

p.primMST(); 
