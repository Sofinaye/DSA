# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            dist_count = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dist_sq = dx * dx + dy * dy
                dist_count[dist_sq] += 1
            
            for count in dist_count.values():
                if count >= 2:
                    res += count * (count - 1)
        return res