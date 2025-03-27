# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution(object):
    def minimumRecolors(self, blocks, k):
        n = len(blocks)
        operation = float("inf")
        temp = 0
        for right in range(k):
            if blocks[right] == 'W':
                temp += 1

        operation = min(operation, temp)
        
        for right in range(k, n):
            if blocks[right] == 'W':
                temp += 1

            if blocks [right - k] == 'W':
                temp -= 1

            operation = min(operation, temp)
            

        return operation

        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        