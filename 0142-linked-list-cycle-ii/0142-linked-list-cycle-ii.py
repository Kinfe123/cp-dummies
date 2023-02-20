# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        
            
        slow = head
        fast = head
        isCycled = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                isCycled = True 
                break
        temp = head 
        
        while temp != slow and slow.next:
            temp = temp.next
            slow = slow.next
        return slow if isCycled else None