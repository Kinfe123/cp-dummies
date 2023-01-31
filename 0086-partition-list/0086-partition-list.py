# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = left_one = ListNode() 
        right = right_one = ListNode()
        while head:
            if head.val < x:
                left_one.next = head
                left_one = left_one.next
            elif head.val >= x:
                right_one.next = head
                right_one = right_one.next
            head = head.next
        
        right_one.next = None
        left_one.next  = right.next
        return left.next
        
        