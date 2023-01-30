# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        left_p , current = dummy , head
        for _ in range(left-1):
            left_p , current = current , current.next
        
        #To get the left previous and current at which left at 
        prev = None
        for _ in range(right - left+1):
            temp = current.next
            current.next = prev
            prev = current 
            current = temp
        
        left_p.next.next = current 
        left_p.next = prev
        return dummy.next