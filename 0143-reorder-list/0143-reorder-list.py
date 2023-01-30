# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #get the middle
        slow , fast = head , head
        if not head: return []
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev , current = None , slow.next
        while current:
            next_c = current.next
            current.next = prev
            prev = current
            current = next_c
        slow.next = None 
        #For avoid the cycle like [1 , 2 , 3 , 4] with [6 , 5 , 4] with is found in both (4)
        #combining the two 
        
        comb1 , comb2 = head  , prev
        while comb2:
            next_1 = comb1.next
            next_2 = comb2.next
            # next_h = comb1.next
            comb1.next = comb2
            comb1 = next_1
        
            comb2.next = comb1
            comb2 = next_2
     
            
        
            
            
            