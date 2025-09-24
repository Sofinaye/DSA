# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0
        self.total = 0  
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.key_values = {}  
    
    def insert(self, key, val):
        old_val = self.key_values.get(key, 0)
        diff = val - old_val
        self.key_values[key] = val
        
        node = self.root
        for char in key:
            node.total += diff
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.total += diff
        node.value = val
    
    def sum(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.total

class MapSum:
    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.sum(prefix)