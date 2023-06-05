#BinarySearchTree
#Pre-Order traversal

class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.key is None:
            self.key = data
        
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

    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

bst = BinarySearchTree(10)
list1 = [6,3,1,6,98,3,7 ]

for i in list1:
    bst.insert(i)

bst.preorder()