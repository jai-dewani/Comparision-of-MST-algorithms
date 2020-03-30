import timeit
from MST.Krushkal import Krushkal
from MST.Prims import Prims
from random import randint

v = randint(100,1000)
edges = []
edge = randint(4*v,10*v)
print("Number of vertices(V): {} | Number of edges: {}".format(v,edge))
for i in range(edge):
    a = [randint(0,v-1),randint(0,v-1),randint(1,10**5)]
    edges.append(a)
'''
v = 4
edges = [
    [0,1,10],
    [0,2,6],
    [0,3,5],
    [1,3,15],
    [2,3,4]
]
'''
print("Krushkal's Algorithms")
k = Krushkal(v)
for i in edges:
    k.addEdge(i[0],i[1],i[2])
time,memory = k.KruskalMST(to_print=False, memory=False)
time_,memory = k.KruskalMST(to_print=False, memory=True)
print("Time:{}s | Memory: {} MB".format(time,memory))


print("Prim's Algorithm")
p = Prims(v) 
p.graph = [[0 for i in range(v)] for j in range(v)]
for i in edges:
    x = i[0]
    y = i[1]
    w = i[2]
    p.graph[x][y] = w
    p.graph[y][x] = w

time1,memory1 = p.primMST(to_print=False,memory=False)
time1_,memory1 = p.primMST(to_print=False,memory=True)
print("Time:{}s Memory: {} MB".format(time1,memory1))

'''
Link to the article -> https://www.geeksforgeeks.org/timeit-python-examples/
setup #Import all the functions you are going to call
stmt #Run those functions
repeat #the number of times you repeat a function
number #calling n number of times in 1 repear
timeit.timeit(setup = setup, stmt = stmt, repeat = repeat, number = number)
'''
