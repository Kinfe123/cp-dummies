# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        temp = temp.next
        summed = 0
        dummy = curr = ListNode()
        start = head
        while temp:
            while temp.val != 0:
                summed+=temp.val
                prev = temp
                temp = temp.next
            curr.next = ListNode(summed)
            curr = curr.next
            temp = temp.next
            
            summed = 0
            
            
        
                
        return dummy.next 
       
#         dummy = curr = ListNode()
#         for i in range(len(result)):
#             curr.next = ListNode(result[i])
#             curr = curr.next
#         curr.next = None
#         return dummy.next
        
    
        