# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lists = []
        temp = head 
        while temp:
            lists.append(temp.val)
            temp = temp.next
        base = 2
        answer = 0
        j = 0
        for i in range(len(lists)-1 , -1 , -1):
            answer+=(lists[i] * (2**(len(lists)-i-1)))
            # result = base ** (len(lists)-i)
            # answer+=(lists[i] * result)
        return answer
        