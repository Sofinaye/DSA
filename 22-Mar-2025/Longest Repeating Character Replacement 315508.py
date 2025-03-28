# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
            
        freq = {}
        max_length = 0
        left = 0
        max_freq = 0
        
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            max_freq = max(max_freq, freq[s[right]])
            
            if (right - left + 1 - max_freq) > k:
                freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        