# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution(object):
    def dividePlayers(self, skill):
        result = []
        total = 0
        left = 0
        skill.sort()
        right = len(skill) - 1
        temp = skill[left] + skill[right] 
        print(skill)
        while left < right:
            if temp != (skill[left] + skill[right]):
                return -1

            total += (skill[left]* skill[right])
            left += 1
            right -= 1

        return total

        """
        :type skill: List[int]
        :rtype: int
        """
        