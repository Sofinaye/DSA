# Problem: Number of Submatrices That Sum to Target - https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
    
        for row in matrix:
            for j in range(1, cols):
                row[j] += row[j - 1]
        
        result = 0
    
        for start_col in range(cols):
            for end_col in range(start_col, cols):
                prefix_sum_count = {0: 1}
                current_sum = 0
                for row in matrix:
                    current_sum += row[end_col] - (row[start_col - 1] if start_col > 0 else 0)
                    result += prefix_sum_count.get(current_sum - target, 0)
                    prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
        
        return result

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        