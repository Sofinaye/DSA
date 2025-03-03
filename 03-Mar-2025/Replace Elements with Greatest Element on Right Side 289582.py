# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution(object):
    def replaceElements(self, arr):
        temp_max = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = arr[i]
            arr[i] = temp_max
            if new_max > temp_max:
                temp_max = new_max

        return arr
        
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        