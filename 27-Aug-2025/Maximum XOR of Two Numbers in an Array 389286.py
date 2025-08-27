# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    def findMaxXOR(self, num):
        node = self.root
        xor_val = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if node.children[toggled_bit]:
                xor_val |= (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children[bit]
        return xor_val
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        max_xor = 0
        for num in nums:
            trie.insert(num)
            max_xor = max(max_xor, trie.findMaxXOR(num))
        return max_xor