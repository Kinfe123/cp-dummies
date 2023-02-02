# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current , previous = head.next , head
        while current:
            if current.val >= previous.val:
                previous = current
                current = current.next
                continue
            temp = dummy 
            # Place to insert 
            while current.val > temp.next.val:
                temp = temp.next
            saver = current.next
            previous.next = current.next
            current.next = temp.next
            temp.next = current
            current = saver
        return dummy.next
            