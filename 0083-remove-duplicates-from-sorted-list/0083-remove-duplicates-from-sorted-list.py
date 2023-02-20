# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            curr = temp.next
            while curr and curr.val == temp.val:
                curr = curr.next
            temp.next = curr
            temp = temp.next
        return head
            
            
            
          