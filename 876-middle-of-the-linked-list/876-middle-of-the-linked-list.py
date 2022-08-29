# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        fast_p = head
        slow_p = head
        while fast_p!= None and fast_p.next != None:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
        
        return slow_p
        