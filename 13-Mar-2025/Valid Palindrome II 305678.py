# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                del_left = s[left + 1: right + 1]

                if del_left == del_left[::-1]:
                    return True

                del_right = s[left : right]

                if del_right == del_right[::-1]:
                    return True
                return False
            left += 1
            right -= 1
        return True
        

        """
        :type s: str
        :rtype: bool
        """
        