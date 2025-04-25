# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []
        result, val = 0, 0
        for p in s:
            if p == "(":
                stack.append(0)
            else:
                mul = stack.pop()
                if mul == 0:
                    val = 1
                else:
                    val = mul * 2

                if not stack:
                    result += val
                else:
                    stack[-1] += val

        return result
        """
        :type s: str
        :rtype: int
        """
        