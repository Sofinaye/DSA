# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        while l1:
            num1 = (num1 * 10) + l1.val
            l1 = l1.next


        num2 = 0
        while l2:
            num2 = (num2 * 10) + l2.val
            l2 = l2.next
        
        result = num1 + num2

        dummy = ListNode(0)
        cur = dummy
        for val in (str(result)):
            cur.next = ListNode(int(val))
            cur = cur.next

        return dummy.next

        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        