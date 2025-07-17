# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        result = ""
        for i in range(len(num)):
            if int(num[i]) % 2:
                result = num[ : i+1]
            
        return result
