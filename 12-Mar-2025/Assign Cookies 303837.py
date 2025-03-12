# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        child = 0
        cookie = 0
        result = 0
        
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                result += 1
                child += 1
            cookie += 1
        
        return result

        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        