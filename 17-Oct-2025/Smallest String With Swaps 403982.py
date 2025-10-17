# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        
        for a, b in pairs:
            uf.union(a, b)
        
        components = {}
        for i in range(n):
            root = uf.find(i)
            if root not in components:
                components[root] = []
            components[root].append(i)
        
        res = [''] * n
        for root, indices in components.items():
            chars = [s[i] for i in indices]
            chars.sort()
            indices.sort()
            for idx, ch in zip(indices, chars):
                res[idx] = ch
        
        return ''.join(res)