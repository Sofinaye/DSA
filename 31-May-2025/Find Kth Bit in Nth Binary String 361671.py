# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution(object):
    def findKthBit(self, n, k):
        def recursive(n, k):
            if n == 1:
                return '0'  
            
            length = (1 << n) - 1  
            mid = length // 2 + 1 
            
            if k == mid:
                return '1'  
            elif k < mid:
                return recursive(n - 1, k)  
            else:
                mirror_k = length - k + 1 
                return '1' if recursive(n - 1, mirror_k) == '0' else '0'
        
        return recursive(n, k)
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        