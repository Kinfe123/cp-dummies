# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None # will be a type of ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_h = set()
        temp = head 
        while temp:
            if temp in set_h:
                return True 
            else:
                
                set_h.add(temp)
            temp = temp.next
        return False
        
           
      
      
        