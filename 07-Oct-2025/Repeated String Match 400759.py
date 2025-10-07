# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not b:
            return 0
        
        min_repeats = (len(b) + len(a) - 1) // len(a)  
        max_repeats = min_repeats + 2
        
        for count in range(min_repeats, max_repeats + 1):
            repeated = a * count
            if b in repeated:
                return count
        
        return -1