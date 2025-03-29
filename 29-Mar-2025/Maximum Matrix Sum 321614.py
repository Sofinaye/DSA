# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution(object):
    def maxMatrixSum(self, matrix):
        n = len(matrix)
        total_abs_sum = 0
        neg_count = 0
        min_abs = float('inf')
        
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                abs_val = abs(val)
                total_abs_sum += abs_val
                if val < 0:
                    neg_count += 1
                if abs_val < min_abs:
                    min_abs = abs_val
        
        if neg_count % 2 == 0:
            return total_abs_sum
        else:
            return total_abs_sum - 2 * min_abs
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        