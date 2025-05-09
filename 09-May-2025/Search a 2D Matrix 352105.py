# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l, r = -1, n * m 
        flag = False
        while l + 1 < r:
            mid = (l + r) // 2
            i = (mid) // m
            j = (mid) % m
            if matrix[i][j] < target:
                l = mid
            else:
                r = mid
        i = (r) // m
        j = (r) % m
        return (target == matrix[i][j]) if r < n * m  else False
