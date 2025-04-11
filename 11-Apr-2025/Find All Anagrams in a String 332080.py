# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution(object):
    def findAnagrams(self, s, p):
        n, m = len(s), len(p)
        left = 0
        result = []
        p_count = [0] * 27
        s_count = [0] * 27
        if len(s) < len(p):
            return []

        for i in range(m):
            index_p = ord(p[i]) - ord("a")
            p_count[index_p] = p_count[index_p] + 1
            
            index_s = ord(s[i]) - ord("a")
            s_count[index_s] = s_count[index_s] + 1

        if p_count == s_count:
            result.append(0)
        
        for right in range(m, n):
            prev_index = ord(s[left]) - ord("a")
            s_count[prev_index] -= 1
            left += 1

            cur_index = ord(s[right]) - ord("a")
            s_count[cur_index] += 1

            if s_count == p_count:
                result.append(left)

        return result
            

        
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        