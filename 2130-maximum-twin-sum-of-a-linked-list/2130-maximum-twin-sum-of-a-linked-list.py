# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lenght = 0
        temp = head 
        while temp:
            temp = temp.next
            lenght+=1
        dummyA = curr = ListNode()
        dummyA.next = head
        temp2 = ListNode()
        dummyA = dummyA.next
        for _ in range(lenght // 2):
            temp2.next = curr
            curr = curr.next

        
        # curr = curr.next
        saver = curr.next
        curr.next = None 
        dummyB = ListNode()
        dummyB.next = saver
        
       
      
        
        dummyB = dummyB.next
        prev , current = None , dummyB
        while current:
            saver = current.next
            current.next = prev
            prev = current
            current = saver
        max_ = 0
        while dummyA and prev:
            summed = dummyA.val+prev.val
            dummyA , prev = dummyA.next , prev.next
            max_ = max(max_ , summed)
        return max_
        
        
        
            
        
            
        
        