# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = []
        count = defaultdict(int)
        for num in arr:
            rem = num % k
            if rem < 0:
                rem += k
            count[rem] += 1
        
        if count[0] % 2 != 0:
            return False
        
        for r in range(1, k//2 + 1):
            if r != k - r:
                if count[r] != count[k - r]:
                    return False
            else:
                if count[r] % 2 != 0:
                    return False
        return True

        