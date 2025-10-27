# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self):
        self.parent = list(range(26))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            # Always point to the smaller root to keep smallest as representative
            if rx < ry:
                self.parent[ry] = rx
            else:
                self.parent[rx] = ry
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
    
        for a, b in zip(s1, s2):
            uf.union(ord(a) - ord('a'), ord(b) - ord('a'))
        
        res = []
        for ch in baseStr:
            root = uf.find(ord(ch) - ord('a'))
            res.append(chr(root + ord('a')))
        
        return ''.join(res)