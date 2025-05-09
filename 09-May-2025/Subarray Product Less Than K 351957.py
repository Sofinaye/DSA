# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
            result = []
            if k <= 1: 
                return 0
            
            count = 0
            prd = 1  
            left = 0   
            
            for right in range(len(nums)):
                prd *= nums[right]  
                while prd >= k:  
                    prd /= nums[left]
                    left += 1
                count += right - left + 1  
            
            return count
        