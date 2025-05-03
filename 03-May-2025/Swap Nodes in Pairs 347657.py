# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur and cur.next:
            nxtpair, second = cur.next.next, cur.next
            second.next = cur
            cur.next = nxtpair
            prev.next = second

            prev = cur
            cur = nxtpair

        return dummy.next
            

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        