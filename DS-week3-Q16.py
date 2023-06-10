class Trienode:
    def __init__(self):
        self.children={}
        self.endofword=False
class Trie:
    def __init__(self):
        self.root=Trienode()
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=Trienode()
            node=node.children[char]
        node.endofword=True
    def search(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.endofword
    def start_with_prefix(self,prefix):
        node=self.root
        for char in prefix:
            if char not in  node.children:
                return []
            node=node.children[char]
        word=[]
        self.dfs(node,prefix,word)
        return word
    def dfs(self,node,prefix,word):
        if node.endofword:
            word.append(prefix)
        for char in node.children:
            self.dfs(node.children[char],prefix+char,word)
t=Trie()
t.insert("sahal")
t.insert("suhail")
t.insert("shafi")
t.insert("fasil")
t.insert("rasak")
print(t.start_with_prefix("s"))
print(t.start_with_prefix("f"))
print(t.start_with_prefix("r"))