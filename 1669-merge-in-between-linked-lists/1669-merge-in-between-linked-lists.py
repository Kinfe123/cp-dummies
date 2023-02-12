
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
            
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp1 = list1
        temp2 = list1
        for i in range(a-1):
            temp1 = temp1.next
            
        for i in range(b):
            temp2 = temp2.next
        temp1.next = list2
        temp3 = list2
        while temp3.next:
            temp3 = temp3.next
        temp3.next = temp2.next
        return list1
            
            
            
        
        
        
        
            
        