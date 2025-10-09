# Problem: Find Beautiful Indices in the Given Array I - https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        A = []
        B = []
        
        len_a, len_b = len(a), len(b)
        
        for i in range(len(s) - len_a + 1):
            if s[i:i+len_a] == a:
                A.append(i)
                
        for i in range(len(s) - len_b + 1):
            if s[i:i+len_b] == b:
                B.append(i)
        
        if not B:
            return []
        
        result = []
        for i in A:
            pos = bisect.bisect_left(B, i - k)
            if pos < len(B) and B[pos] <= i + k:
                result.append(i)
        
        return result
