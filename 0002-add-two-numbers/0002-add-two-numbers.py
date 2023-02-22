# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self , lists):
        prev , curr = None  , lists
        while curr:
            saver = curr.next
            curr.next = prev
            prev = curr
            curr = saver
     
        
        return prev
    def add_(self , list1 ,list2):
        list1_n = []
        list2_n = []
        while list1:
            list1_n.append(list1.val)
            list1 = list1.next
        while list2:
            list2_n.append(list2.val)
            list2 = list2.next
        converted = "".join([str(i) for i in list1_n])
        converted_ = "".join([str(i) for i in list2_n])
        return int(converted)+int(converted_)
    
    
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1  = self.rev(l1)
        list2 = self.rev(l2)
        result = (self.add_(list1 , list2))
        result = list(str(result))
        result.reverse()
        
        
        dummy = curr = ListNode(0)
        for i in range(len(result)):
            curr.next = ListNode(int(result[i]))
            curr = curr.next
        curr.next = None
        return dummy.next
        
        
        
        
        
        