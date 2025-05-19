# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        current = head
        dummy = Node(0)
        copy_current = dummy
        while current:
            copy_current.next = current.next
            copy_current = copy_current.next
            current.next = copy_current.next
            current = current.next
        
        return dummy.next
        