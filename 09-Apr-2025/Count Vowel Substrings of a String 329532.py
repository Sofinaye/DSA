# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution(object):
    def countVowelSubstrings(self, word):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        count = 0

        for i in range(n):
            if word[i] in vowels:
                seen = set()
                for j in range(i, n):
                    if word[j] not in vowels:
                        break
                    seen.add(word[j])
                    if len(seen) == 5:
                        count += 1
        return count
        """
        :type word: str
        :rtype: int
        """
        