# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        s = ""
        ans = []
        for i in searchWord:
            s += i 
            p = [x for x in products if x.startswith(s)]
            p.sort()
            if len(p)<3:
                ans.append(p)
            else:
                ans.append(p[:3])
        return ans