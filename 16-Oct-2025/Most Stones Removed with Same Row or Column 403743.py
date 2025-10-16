# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution(object):
    def removeStones(self, stones):
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        for x, y in stones:
            if x not in parent:
                parent[x] = x
                rank[x] = 0
            if ~y not in parent:
                parent[~y] = ~y
                rank[~y] = 0
            union(x, ~y)

        unique_roots = set(find(x) for x in parent)
        return len(stones) - len(unique_roots)

        """
        :type stones: List[List[int]]
        :rtype: int
        """
        