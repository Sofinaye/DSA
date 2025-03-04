# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution(object):
    def sortPeople(self, names, heights):
        # d = {}
        # result = []
        # for i in range(len(names)):
        #     d[heights[i]] = names[i]
        # heights.sort(reverse=True)
        # for j in heights:
        #     result.append(d[j])
            
        # return result

        people = list(zip(names, heights))

        for i in range(len(people)):
            for j in range(len(people) - 1 - i):
                if people[j][1] < people[j + 1][1]:
                    people[j], people[j + 1] = people[j + 1], people[j]
        result = [individual[0] for individual in people]
        return result

        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        