# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [0] * (len(nums) + 1)
        self.prefix[0] = nums[0]
        for i in range(len(nums)):
            self.prefix[i + 1] = nums[i] + self.prefix[i]


        

    def sumRange(self, left, right):

        return self.prefix[right + 1] - self.prefix[left]
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)