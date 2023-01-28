# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        dummy = ListNode()
        dummy.next = head
        while temp and temp.next:
            while temp and temp.next and temp.val == temp.next.val:
                temp.next = temp.next.next
            temp = temp.next
        return head
        