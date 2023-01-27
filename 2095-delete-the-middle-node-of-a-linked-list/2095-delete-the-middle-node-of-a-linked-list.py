# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        size = 0
        temp = head
        while temp:
            size+=1
            temp = temp.next
        midd = size // 2 
        
        temp2 = head
        prev = None
        index = 0
        dummyNode = ListNode(-1)
        dummyNode.next = head
        current_node = dummyNode
        while current_node.next:
            
            if midd == index:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
            index+=1
        return dummyNode.next
        
            
            
            
        