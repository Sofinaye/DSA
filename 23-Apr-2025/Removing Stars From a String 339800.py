# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution(object):
    def removeStars(self, s):
        st = []
        for char in s:
            if char != "*":
                st.append(char)
            else:
                st.pop()

        return "".join(st)
        """
        :type s: str
        :rtype: str
        """
        