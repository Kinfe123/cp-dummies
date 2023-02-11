# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenght = 0
        temp = head
        while temp:
            lenght+=1
            temp = temp.next
        dummy = temp2 = ListNode()
        dummy.next = head
        i = 0
        while temp2.next:
            if lenght - n == i:
                temp2.next = temp2.next.next
                break
            
            i+=1
            temp2 = temp2.next
        return dummy.next