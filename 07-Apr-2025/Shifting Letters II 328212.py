# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution(object):
    def shiftingLetters(self, s, shifts):
        s = list(s)
        shift = [0]*(len(s)+1)
        sum = 0
        for start , end , dir in shifts:
            if dir == 0:
                shift[start] -= 1
                shift[end+1] += 1

            else:
                shift[start] += 1
                shift[end+1] -= 1

        for i in range(len(s)):
            sum += shift[i]
            s[i] = chr((ord(s[i]) - 97 + sum) % 26 + 97)
        return "".join(s)
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        