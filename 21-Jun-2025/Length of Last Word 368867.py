# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s):
         s = s.strip()
         last_word = s[s.rfind(' ') + 1:]
         return len(last_word)
       
        