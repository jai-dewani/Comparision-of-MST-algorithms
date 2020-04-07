import timeit
from MST.Krushkal import Krushkal
from MST.Prims import Prims
from random import randint
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def edges_build(v,edge):
    edges = []
    for _ in range(edge):
        a = [randint(0,v-1),randint(0,v-1),randint(1,10**5)]
        edges.append(a)
    return edges

def draw_graph(v,edge,pos=None):
    G = nx.Graph()
    G.add_nodes_from(range(v))
    temp = []
    for i in edge:
        temp.append((i[0],i[1]))
    G.add_edges_from(temp)
    if pos is None:
        pos = nx.spring_layout(G)
    nx.draw(G,pos=pos,with_labels=True)
    
    plt.show()
    return pos

kruskal = []
prim = []

Generate_Network_Graph = False
if not Generate_Network_Graph:
    for v in range(100,1000,20):
        # edge = randint(4*v,10*v)
        edge = 10*v
        edges = edges_build(v,edge)
        try:
            k = Krushkal(v)
            for i in edges:
                k.addEdge(i[0],i[1],i[2])
            time,memory,result = k.KruskalMST(to_print=False, memory=False)
            time_,memory,result = k.KruskalMST(to_print=False, memory=True)
            kruskal.append([v,edge,time,memory])
        except:
            pass

        try:
            p = Prims(v) 
            p.graph = [[0 for i in range(v)] for j in range(v)]
            for i in edges:
                x = i[0]
                y = i[1]
                w = i[2]
                p.graph[x][y] = w
                p.graph[y][x] = w
            time1,memory1,result = p.primMST(to_print=False,memory=False)
            time1_,memory1,result = p.primMST(to_print=False,memory=True)
            prim.append([v,edge,time1,memory1])
        except:
            pass
else:
    number_of_edge = 15
    for v in range(number_of_edge,number_of_edge+1):
        # edge = randint(4*v,10*v)
        edge = 10*v
        edges = edges_build(v,edge)
        pos = draw_graph(v,edges)
        try:
            k = Krushkal(v)
            for i in edges:
                k.addEdge(i[0],i[1],i[2])
            time,memory,result = k.KruskalMST(to_print=False, memory=False)
            pos1=draw_graph(v,result,pos)
            time_,memory,result = k.KruskalMST(to_print=False, memory=True)
            kruskal.append([v,edge,time,memory])
        except:
            pass

        try:
            p = Prims(v) 
            p.graph = [[0 for i in range(v)] for j in range(v)]
            for i in edges:
                x = i[0]
                y = i[1]
                w = i[2]
                p.graph[x][y] = w
                p.graph[y][x] = w
            time1,memory1,result = p.primMST(to_print=False,memory=False)
            pos1=draw_graph(v,result,pos)
            time1_,memory1,result = p.primMST(to_print=False,memory=True)
            prim.append([v,edge,time1,memory1])
        except:
            pass
if not Generate_Network_Graph:
    kruskal = np.array(kruskal)
    prim = np.array(prim)

    plt.plot(kruskal[:,0],kruskal[:,3])
    plt.title("kruskal Memory")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Memory (MB)")
    plt.show()

    plt.plot(prim[:,0],prim[:,3])
    plt.title("Prim Memory")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Memory (MB)")
    plt.show()

    plt.plot(kruskal[:,0],kruskal[:,2])
    plt.title("kruskal time")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Time (s)")
    plt.show()

    plt.plot(prim[:,0],prim[:,2])
    plt.title("Prim time")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Time (s)")
    plt.show()

    kruskal_mean_memory = kruskal[:,3].mean()
    prim_mean_memory = prim[:,3].mean()

    kruskal_mean_time = kruskal[:,2].mean()
    prim_mean_time = prim[:,2].mean()
    print(len(kruskal),len(prim))
    print("Kruskal's")
    print("Memory:{}MB | Time:{}s".format(kruskal_mean_memory,kruskal_mean_time))
    print("Prim's")
    print("Memory:{}MB | Time:{}s".format(prim_mean_memory,prim_mean_time))

'''
Link to the article -> https://www.geeksforgeeks.org/timeit-python-examples/
setup #Import all the functions you are going to call
stmt #Run those functions
repeat #the number of times you repeat a function
number #calling n number of times in 1 repear
timeit.timeit(setup = setup, stmt = stmt, repeat = repeat, number = number)
'''
