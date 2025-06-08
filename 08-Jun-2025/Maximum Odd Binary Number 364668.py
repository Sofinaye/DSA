# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution(object):
    def maximumOddBinaryNumber(self, s):
        arr = []
        for i in s:
            if i == "1":
                if  i not in arr:
                    arr.append(i) 
                else:
                    arr.insert(0,i)
            else:
                arr.insert(-1, i)
        return "".join(arr)
        """
        :type s: str
        :rtype: str
        """
        