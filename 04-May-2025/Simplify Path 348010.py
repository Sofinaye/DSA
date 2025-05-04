# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution(object):
    def simplifyPath(self, path):
        stack = []
        components = path.split('/')
        
        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        
        canonical_path = '/' + '/'.join(stack)
        return canonical_path
        """
        :type path: str
        :rtype: str
        """
        