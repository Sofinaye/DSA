# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution(object):
    def removeDuplicateLetters(self, s):
        count = defaultdict(int)
        for char in s:
            count[char] += 1

        stack = []
        visited = set()

        for char in s:
            count[char] -= 1

            if char in visited:
                continue

            while stack and char < stack[-1] and count[stack[-1]] > 0:
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)

        return ''.join(stack)
        """
        :type s: str
        :rtype: str
        """
        