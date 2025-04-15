# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode()
        dummy.next = head
        currNode = dummy

        while currNode and currNode.next:
            if currNode.next.val == val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next

        return dummy.next
        

        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        