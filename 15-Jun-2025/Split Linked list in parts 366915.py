# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        part_size = length // k
        remainder = length % k
        
        current = head
        result = []
        for i in range(k):
            result.append(current)
            size = part_size + (1 if remainder > 0 else 0)
            remainder -= 1
            for _ in range(size - 1):
                if current:
                    current = current.next
            if current:
                next_node = current.next
                current.next = None
                current = next_node
        return result
