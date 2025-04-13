# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ball_colors = {}  
        color_counts = {}  
        result = []
        
        for x, y in queries:
            if x in ball_colors:
                old_color = ball_colors[x]
                color_counts[old_color] -= 1
                
                if color_counts[old_color] == 0:
                    del color_counts[old_color]
            
            ball_colors[x] = y
            
            if y in color_counts:
                color_counts[y] += 1
            else:
                color_counts[y] = 1
            
            result.append(len(color_counts))
        
        return result