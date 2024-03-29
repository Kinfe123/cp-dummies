# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        
        while temp:
            while stack and stack[-1] < temp.val:
                stack.pop()
            stack.append(temp.val)
            temp = temp.next
        dummy = curr =  ListNode()
        
        for i in stack:
            curr.next = ListNode(i)
            curr = curr.next
        curr.next = None
        return dummy.next
        
        