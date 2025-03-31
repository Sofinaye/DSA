# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution(object):
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0]) if m > 0 else 0
        result = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                for x in [i-1, i, i+1]:
                    for y in [j-1, j, j+1]:
                        if 0 <= x < m and 0 <= y < n:
                            total += img[x][y]
                            count += 1
                result[i][j] = total // count
        
        return result
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        