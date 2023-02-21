# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def deleteElements(self  , lists):
        
        
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        dummy.next = head
        while head:
            if head.next and head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                   
                head = head.next
                curr.next = head
            else:
                curr = curr.next
                
                head = head.next
        return dummy.next
                

        
            
        
        
    
                
    
    