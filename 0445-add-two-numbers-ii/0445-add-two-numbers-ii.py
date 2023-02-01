# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        temp1 = l1
        temp2 = l2
        while temp1:
            list1.append(str(temp1.val))
            temp1 = temp1.next
        while temp2:
            list2.append(str(temp2.val))
            temp2 = temp2.next
        
        list1 = int("".join(list1))
        list2 = int("".join(list2))
        summed = list1 + list2
        summed = str(summed)
        summed = [int(x) for x in summed]
        lenght = len(summed)
        dummy =curr = ListNode()
        for i in range(0 , lenght):
            curr.next = ListNode(summed[i])
            curr = curr.next
        return dummy.next
        
        
        
            
        
        