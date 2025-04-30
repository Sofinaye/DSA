# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution(object):
    def superPow(self, a, b):
        mod = 1337
    
        def pow_mod(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                temp = pow_mod(x, n // 2) % mod
                return (temp * temp) % mod
            else:
                return (x % mod) * pow_mod(x, n - 1) % mod
        
        def helper(a, b, index):
            if index == -1:
                return 1
            last_digit = b[index]
            part1 = pow_mod(a, last_digit)
            part2 = pow_mod(helper(a, b, index - 1), 10)
            return (part1 * part2) % mod
        
        return helper(a, b, len(b) - 1)

        
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        