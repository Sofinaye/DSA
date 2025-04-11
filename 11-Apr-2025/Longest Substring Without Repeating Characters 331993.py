# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        longest = 0
        n = len(s)
        checker = set()
        for right in range(n):
            while s[right] in checker:
                checker.remove(s[left])
                left += 1
            w = right - left + 1
            longest = max(longest, w)
            checker.add(s[right])
        
        return longest

        """
        :type s: str
        :rtype: int
        """
        