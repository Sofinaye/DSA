# Problem: Append Characters to String to Make Subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution(object):
    def appendCharacters(self, s, t):
        i = 0
        n = len(t)

        for char in s:
            if i < n and char == t[i]:
                i += 1
