# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index):
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

        """
        :type index: int
        :rtype: int
        """
        

    def addAtHead(self, val):
        head = self.left.next
        node = ListNode(val)
        self.left.next = node
        node.prev = self.left
        node.next = head
        head.prev = node
        """
        :type val: int
        :rtype: None
        """
        

    def addAtTail(self, val):
        node = ListNode(val)
        tail = self.right.prev
        tail.next = node
        node.prev = tail
        node.next = self.right
        self.right.prev = node

        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and index == 0:
            node, next, prev = ListNode(val), cur, cur.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def deleteAtIndex(self, index):
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next

        """
        :type index: int
        :rtype: None
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)