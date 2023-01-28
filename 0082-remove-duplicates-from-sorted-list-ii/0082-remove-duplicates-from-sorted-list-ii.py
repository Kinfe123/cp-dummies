# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def deleteElements(self  , lists):
        
        
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique_l = []
        temp = head
        while temp:
            unique_l.append(temp.val)
            temp = temp.next
        c = Counter(unique_l)
        unique_l = [k for k, v in c.items() if v == 1]
      
        
        dummy = current = ListNode()
        for i in unique_l:
            current.next = ListNode(i)
            current = current.next
        return dummy.next
            
        
        
    
                
    
    