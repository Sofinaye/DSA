# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True
    
    def shortest_root(self, word):
        node = self.root
        prefix = []
        for char in word:
            if char not in node.children:
                return word  
            node = node.children[char]
            prefix.append(char)
            if node.end:
                return ''.join(prefix)
        return word
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        
        words = sentence.split()
        result = []
        for word in words:
            result.append(trie.shortest_root(word))
        
        return ' '.join(result)