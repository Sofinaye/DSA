# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
         duplicates = []
         num_set = set()
         for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                duplicates.append(num)
            
         return duplicates
        #  i = 0
        #  while i < len(nums):
        #      if nums[i] != nums[nums[i] - 1]:  
        #          nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  
        #      else:
        #          i += 1

        #  for i in range(len(nums)):
        #      if nums[i] != i + 1:
        #          duplicates.append(nums[i])

        #  return duplicates

        