# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution(object):
    def clearDigits(self, s):
        result = []
        checker = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for i, char in enumerate(s):
            if char not in checker:
                result.append(char)
            else:
                result.pop()
        return "".join(result)
        """
        :type s: str
        :rtype: str
        """
        