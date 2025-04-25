# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return None

        if not head.next:
            return head

        dummy = head
        index = 0
        while dummy:
            index += 1
            dummy = dummy.next

        n = k % index
        for i in range(n):
            cur = head
            while cur.next.next:
                cur = cur.next

            temp = cur.next
            cur.next = None
            temp.next = head
            head = temp
        return head
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        