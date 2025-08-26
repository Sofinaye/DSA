# Problem: Find Kth Largest XOR Coordinate Value - https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        for x in range(rows):
            for y in range(cols):
                if x > 0:
                    matrix[x][y] ^= matrix[x - 1][y]

        arr = []
        for x in range(rows):
            for y in range(cols):
                if y > 0:
                    matrix[x][y] ^= matrix[x][y-1]
                arr.append(matrix[x][y])
        
        arr.sort()
        arr.reverse()
        return arr[k - 1]