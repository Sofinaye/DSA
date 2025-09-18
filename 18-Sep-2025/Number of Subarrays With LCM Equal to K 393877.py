# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        i = 0
        while i < n:
            if k % nums[i] != 0:
                i += 1
                continue
            j = i
            segment = []
            while j < n and k % nums[j] == 0:
                segment.append(nums[j])
                j += 1
            L = len(segment)
            left = 0
            current_lcm = 1
            for right in range(L):
                current_lcm = current_lcm * segment[right] // math.gcd(current_lcm, segment[right])
                while current_lcm == k and left <= right:
                    total += (L - right)
                    left_lcm = 1
                    for l in range(left+1, right+1):
                        left_lcm = left_lcm * segment[l] // math.gcd(left_lcm, segment[l])
                    current_lcm = left_lcm
                    left += 1
            i = j
        return total