# Problem:  Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"

        res = 0
        mask = 0
        mask_idx = {0: -1}

        for i, c in enumerate(s):
            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord('a'))
            if mask in mask_idx:
                length = i - mask_idx[mask]
                res = max(res, length)
            else:
                mask_idx[mask] = i

        return res