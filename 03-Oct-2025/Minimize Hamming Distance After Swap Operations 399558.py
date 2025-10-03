# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        
        for a, b in allowedSwaps:
            uf.union(a, b)

        components = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            components[root].append(i)
        
        mismatch = 0
        for indices in components.values():
            source_vals = Counter(source[i] for i in indices)
            target_vals = Counter(target[i] for i in indices)
            matches = 0
            for val in set(source_vals) | set(target_vals):
                matches += min(source_vals[val], target_vals[val])
            
            mismatch += len(indices) - matches
        
        return mismatch