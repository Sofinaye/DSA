# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution(object):
    def largestMerge(self, word1, word2):
        merge = []
        i = j = 0
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        merge.extend(word1[i:])
        merge.extend(word2[j:])
        return ''.join(merge)
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        