# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        queue = [(tickets[i], i) for i in range(len(tickets))]
        
        while True:
            cur = queue.pop(0)
            time += 1
            cur_tickets = cur[0] - 1
            if cur[1] == k and cur_tickets == 0:
                return time
            if cur_tickets > 0:
                queue.append((cur_tickets, cur[1]))



        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        