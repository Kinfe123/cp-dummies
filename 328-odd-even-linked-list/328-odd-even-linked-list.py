# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head is None:
            return 
        odd = head
        even = head.next
        evenHead = even
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            
        odd.next = evenHead
        return head
            
            
        