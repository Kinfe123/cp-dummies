# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        d = {0:dummy} 
        while head:
            prefix += head.val
            d[prefix] = head
            head = head.next
	
        head = dummy
        prefix = 0
        
    
        while head:
            prefix += head.val
            head.next = d[prefix].next
            head = head.next
        
        return dummy.next