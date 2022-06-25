from aristas import *
import heapq as hq
import math

def getMin(a):
    min = a[0][1]
    index = 0
    for i, c in enumerate(a):
        if c[1] < min:
            min = c[1]
            index = i
    return a.pop(index)

def definePath(d, path):
    g = []
    g.append(d)

    while path[d] != -1:
        destination = path[d]
        g.insert(0, destination)
        d = destination
    return g

# uses dijkstra
def findShortestPath(graph, s, ignore):
    n = len(graph)
    path = [-1] * n
    visited = [False] * n
    visited[ignore] = True
    
    cost = [math.inf] * n
    cost[s] = 0

    priorityq = [(s, 0)]

    while priorityq:
        # vértice, peso
        u, g = getMin(priorityq)
        if not visited[u]:
            visited[u] = True
        for v, w in graph[u]:
            if not visited[v]:
                weight = g + w
                if weight < cost[v]:
                    cost[v] = weight
                    path[v] = u
                    priorityq.append((v, weight))
    return path, cost

def getDirections(s, d, graph):
    neighbours = graph[s]
    paths = []

    for n in neighbours:
        path, cost = findShortestPath(mapW, n[0], s)
        path = definePath(d, path)
        path.insert(0, s)
        paths.append(path)
        print(path, cost[d])

# desde donde quiero empezar a buscar
source = 299
# a donde quiero llegar
destination = 283
print(getDirections(source, destination, mapW))