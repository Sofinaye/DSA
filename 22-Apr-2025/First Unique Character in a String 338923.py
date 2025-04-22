# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution(object):
    def firstUniqChar(self, s):
        hashMap = {}
        for char in s:
            hashMap[char] = hashMap.get(char,0) + 1
        for j, char in enumerate(s):
            if hashMap[char] == 1:
                return j
        return -1
        """
        :type s: str
        :rtype: int
        """
        