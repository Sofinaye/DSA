# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        rows, cols = len(mat), len(mat[0])
        result = []
        diagonal_dict = {}
        
        for i in range(rows):
            for j in range(cols):
                key = i + j
                if key not in diagonal_dict:
                    diagonal_dict[key] = []
                diagonal_dict[key].append(mat[i][j])
        
        for key in diagonal_dict:
            if key % 2 == 0:
                result.extend(diagonal_dict[key][::-1])  
            else:
                result.extend(diagonal_dict[key])       
        
        return result