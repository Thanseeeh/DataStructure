class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self._find_min_node(node.right)
            node.key = min_node.key
            node.right = self._delete_recursive(node.right, min_node.key)

        return node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        elements = []
        self._inorder_traversal_recursive(self.root, elements)
        return elements

    def _inorder_traversal_recursive(self, node, elements):
        if node:
            self._inorder_traversal_recursive(node.left, elements)
            elements.append(node.key)
            self._inorder_traversal_recursive(node.right, elements)


bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)

print(bst.search(4))
print(bst.search(10)) 

bst.delete(8)
print(bst.inorder_traversal())
