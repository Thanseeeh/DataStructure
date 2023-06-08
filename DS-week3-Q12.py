class Bst:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key is None:
            self.key = data
        elif self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Bst(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Bst(data)

    def search(self, x):
        if self.key == x:
            print("the element is found in the tree")
        elif self.key > x:
            if self.left:
                self.left.search(x)
            else:
                print("element not found")
        else:
            if self.right:
                self.right.search(x)
            else:
                print("element not found")

    def delete(self, x):
        if self.key > x:
            if self.left:
                self.left = self.left.delete(x)
            else:
                print("element not found")
        elif self.key < x:
            if self.right:
                self.right = self.right.delete(x)
            else:
                print("element not found")
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key)
        return self
    
    def min(self):
        if self.key is None:
            print("tree is empty")
            return
        if self.left:
            current = self
            while current.left:
                current = current.left
            print("min = ", current.key)

    def max(self):
        if self.key is None:
            print("tree is empty")
            return
        if self.right:
            current = self
            while current.right:
                current = current.right
            print("max = ", current.key)

    def height(self):
        if self.key is None:
            return 0
        
        left_height = self.left.height()if self.left else 0
        right_height = self.right.height() if self.right else 0

        return max(left_height, right_height) + 1

    def traverse(self):
        print(self.key, "-->", end=" ")
        if self.left:
            self.left.traverse()
        if self.right:
            self.right.traverse()

tree = Bst(10)
tree.insert(20)
tree.insert(30)
tree.insert(2)
tree.insert(33)
tree.insert(18)
tree.insert(66)

tree.delete(20)
tree.min()
tree.max()
tree.traverse()
print()

depth = tree.height()
print(depth)




# class BinaryHeap:
#     def __init__(self):
#         self.heap = []
    
#     def insert(self, data):
#         self.heap.append(data)
#         self.heapify_up(len(self.heap)-1)

#     def heapify_up(self, i):
#         if i==0:
#             return
        
#         parent = (i-1) // 2

#         if self.heap[parent] < self.heap[i]:
#             self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
#             self.heapify_up(parent)
        
#     def extractmax(self):
#         max_value = self.heap[0]
#         self.heap[0] = self.heap[-1]
#         self.heap.pop()
#         self.heapify(0)
#         return max_value
    
#     def delete(self, x):
#         if x not in self.heap:
#             print("element not found")
#         else:
#             index = self.heap.index(x)
#             parent = (index-1) // 2
#             self.heap.pop(index)
#             self.heapify_up(parent)
#             self.heapify(0)

    
#     def heapify(self, i):
#         left = (2*i) + 1
#         right = (2*i) + 2
#         largest = i

#         if left<len(self.heap) and self.heap[left] > self.heap[i]:
#             largest = left
#         if right<len(self.heap) and self.heap[right] > self.heap[largest]:
#             largest = right
        
#         if largest!=i:
#             self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
#             self.heapify(largest)

#     def heap_sort(self):
#         sorted_heap = []
#         while len(self.heap) > 0:
#             max_value = self.extractmax()
#             sorted_heap.insert(0, max_value)
#         return sorted_heap
    
#     def build_heap(self, array):
#         self.heap = array
#         n = len(array)
#         last_parent = (n // 2) -1

#         for i in range(last_parent, -1, -1):
#             self.heapify(i)
#         return self.heap

# heap = BinaryHeap()
# heap.insert(10)
# heap.insert(30)
# heap.insert(12)
# heap.insert(35)
# heap.insert(33)
# heap.insert(2)
# heap.insert(50)
# heap.insert(44)
# heap.insert(26)
# maximum = heap.extractmax()
# print("maximum = ", maximum)
# heap.delete(12)
# print(heap.heap)
# sort = heap.heap_sort()
# print(sort)

# array = [2,3,7,1,4,8,0,81]
# result = heap.build_heap(array)
# print(result)

