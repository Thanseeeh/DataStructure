#BinarySearchTree
class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        
        if self.key > data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = BinarySearchTree(data)

        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = BinarySearchTree(data)

    def search(self, x):
        if self.key is None:
            print("Tree is Empty")
        else:
            if self.key == x:
                print("Element found in Bst")
            elif self.key > x:
                if self.left_child:
                    self.left_child.search(x)
                else:
                    print("Element not found in the tree")
            else:
                if self.right_child:
                    self.right_child.search(x)
                else:
                    print("Element not found in the tree")

    def delete(self, x):
        if self.key is None:
            print("Tree is Empty")
            return
        if self.key > x:
            if self.left_child:
                self.left_child = self.left_child.delete(x)
            else:
                print("Element not found")
        if self.key < x:
            if self.right_child:
                self.right_child = self.right_child.delete(x)
            else:
                print("Element not found")
        else:
            if self.left_child is None:
                temp = self.right_child
                self = None
                return temp
            if self.right_child is None:
                temp = self.left_child
                self = None
                return temp
            node = self.right_child
            while node.left_child:
                node = node.left_child
            self.key = node.key
            self.right_child = self.right_child.delete(node.key)
        return self
    
    def max_node(self):
        if self.key is None:
            print("Tree is Empty")
        else:
            current = self
            while current.right_child:
                current = current.right_child
            return current.key
    
    def min_node(self):
        if self.key is None:
            print("Tree is Empty")
        else:
            current = self
            while current.left_child:
                current =  current.left_child
            return current.key
        
    def height_tree(self):
        if self.key is None:
            return 0
        
        left_child = self.left_child.height_tree() if self.left_child else 0
        right_child = self.right_child.height_tree() if self.right_child else 0

        return max(left_child, right_child) + 1
        
    
    def depth_node(self, x):
        if self.key == x:
            return 0
        
        if self.key > x:
            if self.left_child:
                return self.left_child.depth_node(x) + 1
            else:
                return -1
            
        if self.key < x:
            if self.right_child:
                return self.right_child.depth_node(x) + 1
            else:
                return -1

    def pre_order(self):
        if self.key is None:
            print("Tree is Empty")
        else:
            print(self.key, "-->", end=" ")
            if self.left_child:
                self.left_child.pre_order()
            if self.right_child:
                self.right_child.pre_order()

    def in_order(self):
        if self.key is None:
            print("Tree is Empty")
        else:
            if self.left_child:
                self.left_child.in_order()
            print(self.key, "-->", end=" ")
            if self.right_child:
                self.right_child.in_order()

    def post_order(self):
        if self.key is None:
            print("Tree is Empty")
        else:
            if self.left_child:
                self.left_child.post_order()
            if self.right_child:
                self.right_child.post_order()
            print(self.key, "-->", end=" ")

bst = BinarySearchTree(12)
bst.insert(15)
bst.insert(45)
bst.insert(32)
bst.insert(26)
bst.insert(99)

print("_____________________________________________________________________________")
print()
print("Pre-Order Traversal  : ", end=" ")
bst.pre_order()
print()
print()
print("In-Order Traversal   : ", end=" ")
bst.in_order()
print()
print()
print("In-Order Traversal   : ", end=" ")
bst.post_order()
print()
print()
max_value = bst.max_node()
print("highest value    = ", max_value)
min_value = bst.min_node()
print("lowest value     = ", min_value)
height = bst.height_tree()
print("height of tree   = ", height)
depth = bst.depth_node(15)
print("depth of node    = ", depth)
print("_____________________________________________________________________________")





#BinaryHeap
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self, i):
        if i == 0:
            return
        
        parent = (i-1) // 2

        if self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.heapify_up(parent)

    def max_heap(self):
        if self.heap is None:
            print("Heap is empty")
        else:
            return self.heap[0]
        
    def extract_max(self):
        if self.heap is None:
            print("Heap is empty")
        else:
            max_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.heapify(0)
            return max_val
        
    def delete(self, x):
        if self.heap is None:
            print("Heap is empty")
        else:
            if x in self.heap:
                index = self.heap.index(x)
                parent = (index - 1) // 2
                self.heap.pop(index)
                self.heapify_up(parent)
                self.heapify(0)
        
    def heapify(self, i):
        left = (2*i) + 1
        right = (2*i) + 2
        largest = i

        if left < len(self.heap) and self.heap[left] > self.heap[i]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.heapify(largest)

    def heap_sort(self):
        sorted_heap = []
        while len(self.heap) > 0:
            max_val = self.extract_max()
            sorted_heap.insert(0, max_val)
        return sorted_heap
    
    def build_heap(self, array):
        self.heap = array
        n = len(array)
        last_parent = (n//2) - 1

        for i in range(last_parent, -1, -1):
            self.heapify(i)
        return self.heap

heap = MaxHeap()
heap.insert(12)
heap.insert(15)
heap.insert(33)
heap.insert(9)
heap.insert(21)
print()
print("Binary Heap = ",end=" ")
print(heap.heap)
print()
maximum = heap.max_heap()
print("Max value        = ", maximum)
print("Extracted max    = ", end=" ")
heap.extract_max()
print(heap.heap)
print("Node deleted     = ", end=" ")
heap.delete(12)
print(heap.heap)
print("Sorted Heap      = ", end=" ")
sort = heap.heap_sort()
print(sort)

array = [4,3,1,7,4,6,1]
build_heap = heap.build_heap(array)
print("New Heap builded = ", end=" ")
print(build_heap)
print("_____________________________________________________________________________")





#Graph
class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, v):
        if v in self.graph:
            print("Node is already present")
        else:
            self.graph[v] = []
    
    def add_edge(self, v1, v2):
        if v1 not in self.graph or v2 not in self.graph:
            print("These elements not found in graph")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def delete_node(self, v):
        if v not in self.graph:
            print("Element not found")
        else:
            self.graph.pop(v)
            for i in self.graph:
                if v in self.graph[i]:
                    self.graph[i].remove(v)

    def delete_edge(self, v1, v2):
        if v1 not in self.graph or v2 not in self.graph:
            print("These elements not found in graph")
        else:
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)

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

    def dfs_all(self):
        self.visited = []
        for i in self.graph:
            if i not in self.visited:
                self.dfs(i)

graph = Graph()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)

graph.add_edge(1,4)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(2,1)

print()
print("Graph        = ", end=" ")
print(graph.graph)
print("Node deleted = ", end=" ")
graph.delete_node(2)
print(graph.graph)
print("Edge deleted = ", end=" ")
graph.delete_edge(1,4)
print(graph.graph)

print("Bfs of graph = ", end=" ")
graph.bfs_all()
print()
print("Dfs of graph = ", end=" ")
graph.dfs_all()