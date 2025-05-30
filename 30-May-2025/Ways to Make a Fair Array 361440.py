# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even = [0]*(len(nums)+1)
        odd = [0]*(len(nums)+1)
        for i in range(len(nums)):
            if i%2==0:
                even[i]+=even[i-1]+nums[i]
                odd[i] = odd[i-1]
            else:
                odd[i]+=odd[i-1]+nums[i]
                even[i] = even[i-1]
                
        ev,od = 0,0 
        ans = 0
        for i in range(len(nums)):
            ev = even[i-1]
            od = odd[i-1]
            ev += odd[len(nums)-1] - odd[i]
            od += even[len(nums)-1] - even[i]
            if ev==od:
                ans+=1
        return ans

        