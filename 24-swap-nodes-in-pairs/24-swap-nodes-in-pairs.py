# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        temp = head
        if temp is None:
            return 
        while temp and temp.next:
            if temp.val != temp.next.val:
                temp.val , temp.next.val = temp.next.val , temp.val
            
            
            temp = temp.next.next
            
        return head
                
        
        