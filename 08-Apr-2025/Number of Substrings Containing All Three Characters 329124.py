# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution(object):
    def numberOfSubstrings(self, s):
        count = 0
        start_a = start_b = start_c = -1

        for i, char in enumerate(s):
            if char == "a":
                start_a = i
            elif char == "b":
                start_b = i
            else:
                start_c = i


            least_of_all_index = min(start_a, start_b, start_c)

            if least_of_all_index != -1:
                	count += 1 + least_of_all_index
        return count
        """
        :type s: str
        :rtype: int
        """
        