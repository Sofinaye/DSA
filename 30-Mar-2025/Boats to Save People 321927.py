# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats

        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        