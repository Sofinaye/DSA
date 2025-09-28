# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        l, r =0, 0
        n = len(s)
        ans = []
        checker = set()
        while r < n:
            if not s[l:r+1] in checker:
                checker.add(s[l:r+1])
                ans.append(s[l:r+1])
                l=r+1
                r+=1
            else:
                r+=1
        return ans