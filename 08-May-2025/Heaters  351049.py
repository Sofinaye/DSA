# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius = 0
        for house in houses:
            index = bisect.bisect_left(heaters, house)
            min_dist = float('inf')
            if index > 0:
                min_dist = min(min_dist, house - heaters[index - 1])
            if index < len(heaters):
                min_dist = min(min_dist, heaters[index] - house)
            max_radius = max(max_radius, min_dist)
        return max_radius