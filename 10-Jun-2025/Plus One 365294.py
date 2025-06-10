# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        for num in digits:
            result *= 10
            result += num
        
        result += 1
        output = []
        while result >= 10:
            temp = result % 10
            output.append(temp)
            result //= 10
        output.append(result % 10)
        return output[::-1]

        