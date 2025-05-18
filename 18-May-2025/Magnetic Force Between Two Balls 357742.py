# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        left, right = 1, position[-1] - position[0]
        answer = 0
        
        def is_possible(min_force):
            count = 1
            last_position = position[0]
            for i in range(1, n):
                if position[i] - last_position >= min_force:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return count >= m
        
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer