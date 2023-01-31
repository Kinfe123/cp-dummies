# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head
        counter = 1
        
        tmp_tail = head
        while tmp_tail.next:
            tmp_tail = tmp_tail.next
            counter += 1
        k = k % counter
        if k == 0:
            return head
        to_go = counter - k - 1
        tmp_curr = head 
        while to_go > 0:
            tmp_curr = tmp_curr.next
            to_go-=1
            
        result = tmp_curr.next
        
        tmp_curr.next = None
        
        tmp_tail.next = head
        return result
        
        
        
        