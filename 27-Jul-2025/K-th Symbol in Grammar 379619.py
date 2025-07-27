# Problem: K-th Symbol in Grammar - https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        if parent == 0:
            return 0 if k % 2 == 1 else 1
        else:
            return 1 if k % 2 == 1 else 0