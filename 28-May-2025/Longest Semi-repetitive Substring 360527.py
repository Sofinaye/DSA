# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n
        
        max_len = 1
        left = 0
        pair_count = 0
        
        for right in range(1, n):
            if s[right] == s[right - 1]:
                pair_count += 1
            
            while pair_count > 1:
                if s[left] == s[left + 1]:
                    pair_count -= 1
                left += 1
            
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        
        return max_len