# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
    
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))
        
        dummy = ListNode(0)
        current = dummy
        while min_heap:
            val, list_idx, node = heapq.heappop(min_heap)
            
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_idx, node.next))
        
        return dummy.next