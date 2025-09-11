# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_count = 0
        i = 0
        while i < n:
            if nums[i] % k != 0:
                i += 1
                continue
            j = i
            segment = []
            while j < n and nums[j] % k == 0:
                segment.append(nums[j])
                j += 1
            L = len(segment)
            for start in range(L):
                current_gcd = 0
                for end in range(start, L):
                    current_gcd = math.gcd(current_gcd, segment[end])
                    if current_gcd == k:
                        total_count += 1
            i = j
        return total_count