# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) == k:
                result.append(path.copy())
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        
        result = []
        backtrack(1, [])
        return result