# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def backtrack(s: str, start: int, prev_num: int) -> bool:
            if start == len(s):
                return True
            current_num = 0
            for i in range(start, len(s)):
                current_num = current_num * 10 + int(s[i])
                if current_num == prev_num - 1:
                    if backtrack(s, i + 1, current_num):
                        return True
                elif current_num > prev_num - 1:
                    break
            return False

        for i in range(1, n):
            first_num = int(s[:i])
            if backtrack(s, i, first_num):
                return True
        return False