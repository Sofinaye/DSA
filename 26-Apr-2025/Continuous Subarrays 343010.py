# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution(object):
    def continuousSubarrays(self, nums):
        ans = 0
        minq = deque()
        maxq = deque()

        left = 0

        for right in range(len(nums)):
            x = nums[right]
            while len(minq) > 0 and minq[-1] > x:
                minq.pop()

            minq.append(x)

            while len(maxq) > 0 and maxq[-1] < x:
                maxq.pop()

            maxq.append(x)

            while maxq[0] - minq[0] > 2:
                if minq[0] == nums[left]:
                    minq.popleft()
                if maxq[0] == nums[left]:
                    maxq.popleft()

                left += 1

            ans += (right - left + 1)

        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        