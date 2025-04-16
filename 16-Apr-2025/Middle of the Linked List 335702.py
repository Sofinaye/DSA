# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        