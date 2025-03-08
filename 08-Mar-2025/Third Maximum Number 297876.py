# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution(object):
    def thirdMax(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        distinct = []
        for val in count:
            distinct.append(val)

        n = len(distinct)
        distinct.sort()

        return distinct[-3] if n > 2 else distinct[-1]



        """
        :type nums: List[int]
        :rtype: int
        """