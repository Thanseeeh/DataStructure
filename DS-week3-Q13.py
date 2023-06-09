class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = set()

    def addNode(self, v):
        if v in self.graph:
            print("Node already in graph")
        else:
            self.graph[v] = []

    def addEdge(self, v1, v2):
        if v1 not in self.graph or v2 not in self.graph:
            print("Node(s) not found in graph")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def deleteNode(self, v):
        if v not in self.graph:
            print("Node not found in graph")
        else:
            self.graph.pop(v)
            for i in self.graph:
                if v in self.graph[i]:
                    self.graph[i].remove(v)

    def deleteEdge(self, v1, v2):
        if v1 not in self.graph or v2 not in self.graph:
            print("Edge not found in graph")
        else:
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)

    def dfs_iterative(self, v):
        if v not in self.graph:
            print("Node not found")
            return
        stack = [v]
        while stack:
            temp = stack.pop()
            if temp not in self.visited:
                print(temp)
                self.visited.add(temp)
                for i in self.graph[temp]:
                    stack.append(i)

    def bfs(self, start):
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in self.visited:
                print(node)
                self.visited.add(node)
                b = self.graph[node]
                for temp in b:
                    if temp not in self.visited:
                        queue.append(temp)


graph = Graph()
graph.addNode(1)
graph.addNode(2)
graph.addNode(3)
graph.addNode(4)
graph.addNode(5)
graph.addNode(7)
graph.addNode(6)
print(graph.graph)
graph.addEdge(1, 5)
graph.addEdge(1, 4)
graph.addEdge(1, 2)
graph.addEdge(2, 7)
graph.addEdge(2, 6)
graph.addEdge(2, 3)
print(graph.graph)
graph.bfs(1)