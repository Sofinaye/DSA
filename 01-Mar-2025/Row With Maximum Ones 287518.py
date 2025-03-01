# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution(object):
    def rowAndMaximumOnes(self, mat):
        count = 0
        index = 0
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            streak = 0
            for j in range(n):
                if mat[i][j] == 1:
                    streak += 1
                if streak > count:
                    count = streak
                    index = i

        return [index, count]
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        