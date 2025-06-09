# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        return haystack.find(needle)
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        