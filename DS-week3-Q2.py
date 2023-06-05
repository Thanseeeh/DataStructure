#BinarySearchTree
#Insertion and Searching

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
        if self.key == x:
            print("Element is found")
        elif self.key > x:
            if self.left_child:
                self.left_child.search(x)
            else:
                print("Element not found")
        else:
            if self.right_child:
                self.right_child.search(x)
            else:
                print("Element not found")

bst = BinarySearchTree(10)
list1 = [4,9,15,34,13,11]

for i in list1:
    bst.insert(i)

bst.search(15)