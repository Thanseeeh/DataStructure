#BinarySearchTree
#Delete element

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

    def delete(self, x):
        if self.key is None:
            print("Binary tree is empty")
            return
        
        elif self.key > x:
            if self.left_child:
                self.left_child = self.left_child.delete(x)
            else:
                print("given node not present in the tree")
        
        elif self.key < x:
            if self.right_child:
                self.right_child = self.right_child.delete(x)
            else:
                print("given node not present in the tree")
            
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

    def traverse(self):
        print(self.key)
        if self.left_child:
            self.left_child.traverse()
        if self.right_child:
            self.right_child.traverse()

bst = BinarySearchTree(10)
list1 = [3,2,6,1,9,10,4]

for i in list1:
    bst.insert(i)

bst.delete(6)
bst.traverse()