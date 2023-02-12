# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        temp = temp.next
        result = []
        summed = 0
        while temp:
            while temp.val != 0:
                summed+=temp.val
                temp = temp.next
            result.append(summed)
            summed = 0
            temp = temp.next
       
        dummy = curr = ListNode()
        for i in range(len(result)):
            curr.next = ListNode(result[i])
            curr = curr.next
        curr.next = None
        return dummy.next
        
    
        