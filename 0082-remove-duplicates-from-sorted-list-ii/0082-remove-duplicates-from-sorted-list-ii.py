# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        element_ = set()
        while temp and temp.next:
            curr = temp.next
            
            while curr and curr.val == temp.val:
                element_.add(curr.val)
                curr = curr.next
            
            temp.next = curr
            temp = temp.next
       
        dummy = curr = ListNode(0)
        dummy.next = head
      
    
        while curr and curr.next:
            if curr.next.val in element_:
            
                curr.next = curr.next.next
                curr = curr
            else:
                curr = curr.next
        return dummy.next
        
            
            
                
                
                
        
        