class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, v):
        if v in self.graph:
            print("element is already exist")
        else:
            self.graph[v] = []

    def add_edge(self, v1, v2):
        if v1 not in self.graph or v2 not in self.graph:
            print("elements not found")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def delete_node(self, v):
        if v not in self.graph:
            print("element is unknown")
        else:
            self.graph.pop(v)
            for i in self.graph:
                if v in self.graph[i]:
                    self.graph[i].remove(v)

    def delete_edge(self, v1, v2):
        if v1 not in self.graph or v2 not in self.graph:
            print("elemtns not found")
        else:
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)

    def bfs(self, start):
        self.visited = []
        queue = []
        self.visited.append(start)
        queue.append(start)

        while queue:
            v = queue.pop(0)
            print(v, end=" ")
            for neighbor in self.graph[v]:
                if neighbor not in self.visited:
                    queue.append(neighbor)
                    self.visited.append(neighbor)

    def bfs_all(self):
        self.visited = []
        for i in self.graph:
            if i not in self.visited:
                self.bfs(i)

    def dfs(self, start):
        self.visited = []
        self._dfs(start)

    def _dfs(self, v):
        self.visited.append(v)
        print(v, end=" ")
        for i in self.graph[v]:
            if i not in self.visited:
                self._dfs(i)

graph = Graph()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(7)
graph.add_node(6)
print(graph.graph)
graph.add_edge(1, 5)
graph.add_edge(1, 4)
graph.add_edge(1, 2)
graph.add_edge(2, 7)
graph.add_edge(2, 6)
graph.add_edge(2, 3)
print(graph.graph)
graph.bfs_all()
print()
graph.dfs(2)