# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution(object):
    def flipAndInvertImage(self, image):
        n = len(image)
        for i in range(n):
            for j in range(n//2):
                image[i][j], image[i][n - j - 1] = image[i][n - j - 1], image[i][j]
        
        for i in range(n):
            for j in range(n):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        