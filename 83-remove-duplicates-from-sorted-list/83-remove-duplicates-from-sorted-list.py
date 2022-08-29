# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        if temp is None:
            return 
        while temp.next is not None:
            if temp.val == temp.next.val:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return head
                
        