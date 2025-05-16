# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            bouquets = 0
            flowers = 0
            for d in bloomDay:
                if d <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                        if bouquets >= m:
                            break
                else:
                    flowers = 0
            if bouquets >= m:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
