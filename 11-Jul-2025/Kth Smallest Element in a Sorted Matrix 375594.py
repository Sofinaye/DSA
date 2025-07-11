# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        
        while left < right:
            mid = (left + right) // 2
            count = 0
            i, j = 0, n - 1
            while i < n and j >= 0:
                if matrix[i][j] <= mid:
                    count += j + 1
                    i += 1
                else:
                    j -= 1
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left