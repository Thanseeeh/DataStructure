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