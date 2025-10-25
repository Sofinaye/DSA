# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = [-p for p in piles]
        heapq.heapify(h)
        for _ in range(k):
            largest = -heapq.heappop(h) 
            largest -= largest//2
            heapq.heappush(h,-largest)
        return -sum(h)