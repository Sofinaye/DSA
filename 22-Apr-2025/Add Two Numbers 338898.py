# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        carry = 0
        curr1, curr2 = l1, l2

        while curr1 or curr2:

            if curr1:
                val1 = curr1.val
            else:
                val1 = 0

            if curr2:
                val2 = curr2.val
            else:
                val2 = 0
            curr = val1 + val2 + carry
            rem = curr % 10
            cur.next = ListNode(rem)
            carry = curr // 10
            
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            cur = cur.next

        if carry != 0:
            cur.next = ListNode(carry)
            
        return dummy.next



        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        