class Trienode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Trienode()
            node = node.children[char]
        node.endofword = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.endofword

    def start_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        words = []
        self.dfs(node, prefix, words)
        return words

    def dfs(self, node, prefix, words):
        if node.endofword:
            words.append(prefix)
        for char in node.children:
            self.dfs(node.children[char], prefix + char, words)

    def delete(self, word):
        if not self.search(word):
            print("Word not found in Trie.")
            return
        self._delete(self.root, word, 0)

    def _delete(self, node, word, index):
        if index == len(word):
            node.endofword = False
            if not node.children:
                del node
            return

        char = word[index]
        if char not in node.children:
            return

        child_node = node.children[char]
        self._delete(child_node, word, index + 1)

        if not child_node.children and not child_node.endofword:
            del node.children[char]



t = Trie()
t.insert("sahal")
t.insert("suhail")
t.insert("shafi")
t.insert("fasil")
t.insert("rasak")

print(t.start_with_prefix("s"))
t.delete("suhail")
print(t.start_with_prefix("s"))
