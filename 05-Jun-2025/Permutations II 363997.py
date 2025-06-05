# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        count = Counter(nums)
        def dfs():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            for n in count:
                if count[n] > 0:
                    permutation.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    permutation.pop()
        dfs()
        return res