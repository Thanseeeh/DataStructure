class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = []

    def addnode(self, v):
        if v in self.graph:
            print("Node already in the graph")
        else:
            self.graph[v] = []

    def addedge(self, v1, v2):
        if v1 not in self.graph or v2 not in self.graph:
            print("Nodes are not in the graph")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def deleteNode(self, v):
        if v not in self.graph:
            print("Element not found")
        else:
            self.graph.pop(v)
            for i in self.graph:
                if v in self.graph[i]:
                    self.graph[i].remove(v)

    def deleteEdge(self, v1, v2):
        if v1 not in self.graph or v2 not in self.graph:
            print("Elements not found in graph")
        else:
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)

    def dfs(self, start):
        self.visited = []
        self._dfs(start)

    def _dfs(self, v):
        self.visited.append(v)
        print(v, end=" ")
        for neighbor in self.graph[v]:
            if neighbor not in self.visited:
                self._dfs(neighbor)

    def bfs(self, start):
        self.visited = []
        queue = []
        queue.append(start)
        self.visited.append(start)

        while queue:
            v = queue.pop(0)
            print(v, end=" ")
            for neighbor in self.graph[v]:
                if neighbor not in self.visited:
                    queue.append(neighbor)
                    self.visited.append(neighbor)


# Usage example
graph = Graph()

graph.addnode(1)
graph.addnode(2)
graph.addnode(3)
graph.addnode(4)
graph.addnode(5)
print(graph.graph)
graph.addedge(2, 3)
graph.addedge(3, 1)
graph.addedge(4,1)
graph.addedge(4,5)
graph.addedge(5,1)
print(graph.graph)

print("DFS:")
graph.dfs(4)
print("\nBFS:")
graph.bfs(4)