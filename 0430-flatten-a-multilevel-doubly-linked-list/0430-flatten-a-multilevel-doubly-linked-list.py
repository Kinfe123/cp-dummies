
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummyNode = ListNode(0)
        dummyNode.next = head
        childFounder = []
        while head:
            if head.child:
                if head.next:
                    childFounder.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
                
                    
            
            while childFounder and not head.next:
                popped = childFounder.pop()
                head.next = popped
                head.next.prev = head
                # head.child = None
            head = head.next
        return dummyNode.next
                
        