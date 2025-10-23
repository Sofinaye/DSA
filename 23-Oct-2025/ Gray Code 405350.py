# Problem:  Gray Code - https://leetcode.com/problems/gray-code/description/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        prev = self.grayCode(n-1)
        result = list(prev)
        mask = 1 << (n-1)
        for code in reversed(prev):
            result.append(code | mask)
        return result