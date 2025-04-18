# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next

        return result == result[::-1]
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        