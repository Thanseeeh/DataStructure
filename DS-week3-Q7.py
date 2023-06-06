#All operations in BinarySearchTree

class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        
        elif self.key > data:
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
            print("Tree is empty")
            return
        if self.key == x:
            print("Element is in Tree")
            return
        elif self.key > x:
            if self.left_child:
                self.left_child.search(x)
            else:
                print("Element not found in Tree")
        else:
            if self.right_child:
                self.right_child.search(x)
            else:
                print("Element not found in Tree")

    def delete(self, x):
        if self.key is None:
            print("Tree is Empty")
            return
        
        if self.key > x:
            if self.left_child:
                self.left_child = self.left_child.delete(x)
            else:
                print("Element not found in the Tree")

        elif self.key < x:
            if self.right_child:
                self.right_child = self.right_child.delete(x)
            else:
                print("Element not found in the Tree")

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
    
    def max_value(self):
        if self.key is None:
            print("Tree is Empty")
            return
        if self.right_child:
            current = self
            while current.right_child:
                current = current.right_child
            return current.key
        
    def min_value(self):
        if self.key is None:
            print("Tree is Empty")
            return
        if self.left_child:
            current = self
            while current.left_child:
                current = current.left_child
            return current.key
    
    def preorder(self):
        print(self.key, " - ", end="")
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.key, " - ", end="")
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key, " - ", end="")

tree = BinarySearchTree(10)
list1 = [3,78,4,34,11,9]
for i in list1:
    tree.insert(i)

tree.search(4)
tree.delete(11)
max = tree.max_value()
print("Maximum = ",max)
min = tree.min_value()
print("Minimum = ", min)
print()

print("Pre-order")
tree.preorder()
print()

print("In-order")
tree.inorder()
print()

print("Post-order")
tree.postorder()
print()