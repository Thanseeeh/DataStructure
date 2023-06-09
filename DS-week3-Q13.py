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