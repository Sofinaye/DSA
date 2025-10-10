# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        cur = 0
        power_k = pow(power, k, modulo)
        idx = 0

        for i in range(n - 1, -1, -1):
            cur = (cur * power + (ord(s[i]) - 96)) % modulo
            if i + k < n:
                cur = (cur - (ord(s[i + k]) - 96) * power_k) % modulo
            if cur == hashValue:
                idx = i
        return s[idx:idx + k]