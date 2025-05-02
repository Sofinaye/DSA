# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution(object):
    def pairSum(self, head):
        dummy = head
        temp = None
        tail = None
        while dummy:
            if not dummy.next:
                tail = dummy
            dummy.prev = temp
            temp = dummy
            dummy = dummy.next
            
        dummy = head
        result = 0
        while dummy.prev != tail:
            cur_sum = dummy.val + tail.val
            result = max(result, cur_sum)
            dummy = dummy.next
            tail = tail.prev
        
        return result

             

        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        