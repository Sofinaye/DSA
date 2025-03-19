# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution(object):
    def appendCharacters(self, s, t):
        i = 0
        n = len(t)

        for char in s:
            if i < n and char == t[i]:
                i += 1

        return n - i 
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        