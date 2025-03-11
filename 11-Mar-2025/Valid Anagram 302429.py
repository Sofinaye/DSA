# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        collectionS, collectionT = {}, {}
        for i in range(len(s)):
            collectionS[s[i]] = collectionS.get(s[i],0) + 1
            collectionT[t[i]] = collectionT.get(t[i],0) + 1
        for j in collectionS:
            if collectionS[j] != collectionT.get(j,0):
                return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        