# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        if x not in self.parent:
            self.parent[x] = x
        if y not in self.parent:
            self.parent[y] = y
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name
        
        groups = defaultdict(list)
        for email in uf.parent:
            root = uf.find(email)
            groups[root].append(email)
        
        res = []
        for root, emails in groups.items():
            res.append([email_to_name[root]] + sorted(emails))
        
        return res