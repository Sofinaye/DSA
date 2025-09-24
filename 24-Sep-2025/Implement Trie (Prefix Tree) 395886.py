# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self):
        self.children = [None for x in range(26)]
        self.end = False
class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not current.children[idx]:
                current.children[idx] = Node()
            current = current.children[idx]
        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not current.children[idx]:
                return False
            current = current.children[idx]
        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if not current.children[idx]:
                return False
            current = current.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)