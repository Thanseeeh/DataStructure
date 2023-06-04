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