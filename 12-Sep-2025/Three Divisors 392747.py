# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
     def isThree(self, n: int) -> bool:
        res = [1]
        prime = 2

        while n >= prime :
            if n % prime == 0:
                res.append(prime)
            prime += 1

        if len(res) == 3:
            return True
        return False
        
        