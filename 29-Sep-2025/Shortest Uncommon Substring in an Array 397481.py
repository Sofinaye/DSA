# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sources = set()
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, source):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sources.add(source)
    def get_sources(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return set()
            node = node.children[char]
        return node.sources
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        trie = Trie()
        
        for idx, s in enumerate(arr):
            length = len(s)
            for start in range(length):
                for end in range(start + 1, length + 1):
                    substr = s[start:end]
                    trie.insert(substr, idx)
        
        result = [""] * n
        
        for i in range(n):
            s = arr[i]
            length = len(s)
            found = None
            for sub_len in range(1, length + 1):
                candidates = []
                for start in range(length - sub_len + 1):
                    substr = s[start:start + sub_len]
                    sources = trie.get_sources(substr)
                    if sources == {i}:
                        candidates.append(substr)
                if candidates:
                    found = min(candidates)
                    break
            if found:
                result[i] = found
        
        return result
        