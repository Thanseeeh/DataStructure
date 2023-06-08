def addNode(v):
    if v in graph:
        print("already i graph")
    else:
        graph[v] = []


def addEdge(v1, v2):
    if v1 and v2 not in graph:
        print("not found in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def deletenode(v):
    if v not in graph:
        print("not found in graph")
    else:
        graph.pop(v)
        for i in graph:
            if v in graph[i]:
                graph[i].remove(v)


def deleteedge(v1, v2):
    if v1 and v2 not in graph:
        print("edge not found in graph")
    else:
        graph[v1].remove(v2)
        graph[v2].remove(v1)


def dfs_iterative(v, graph):
    if v not in graph:
        print("value not found")
        return
    stack = [v]
    while stack:
        temp = stack.pop()
        if temp not in visited:
            print(temp)
            visited.add(temp)
            for i in graph[temp]:
                stack.append(i)


def bfs(graph, start):
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:

            print(node)
            visited.add(node)
            b=graph[node]

        for temp in b:
            if temp not in visited:
                queue.append((temp))




visited = set()
graph = {}
addNode(1)
addNode(2)
addNode(3)
addNode(4)
addNode(5)
addNode(7)
addNode(6)
print(graph)
addEdge(1, 5)
addEdge(1, 4)
addEdge(1, 2)
addEdge(2, 7)
addEdge(2, 6)
addEdge(2, 3)

print(graph)
print(bfs(graph,1))