# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0

        for j in range(26):
            if s1_count[j] == s2_count[j]:
                matches += 1

        left = 0
        
        for right in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[right]) - ord("a")
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            index = ord(s2[left]) - ord("a")
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1

            left += 1

        return matches == 26




        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        