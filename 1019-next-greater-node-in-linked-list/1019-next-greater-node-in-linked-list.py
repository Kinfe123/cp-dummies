# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        dummy = curr =ListNode()
        collector = []
        
        while head:
            while stack and stack[-1][1] < head.val:
                indx_ = stack.pop()[0]
                collector[indx_] = head.val
                
            stack.append([len(collector) , head.val])
            collector.append(0)
            head = head.next
                
        return collector
    
        
            
        