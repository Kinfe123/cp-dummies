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
                    #Deleting the top of the head 
                #when it goes out of the loop we should not have to include the one that 
                #has a duplicate and move it to the next and attach the rest to curr -
                head = head.next
                curr.next = head
            else:
                curr = curr.next
                
                head = head.next
        return dummy.next
                

        
            
        
        
    
                
    
    