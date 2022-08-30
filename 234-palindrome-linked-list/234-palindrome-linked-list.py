# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        def reverse(head):
            curr , prev = head , None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        secondHalfHead = reverse(slow.next)
        firstHalfHead = head
        while secondHalfHead is not None and firstHalfHead is not None:
            if firstHalfHead.val != secondHalfHead.val:
                return False
            secondHalfHead = secondHalfHead.next
            firstHalfHead = firstHalfHead.next
            
        return True
    
        
        
        
        