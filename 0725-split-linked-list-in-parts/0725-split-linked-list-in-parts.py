# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head 
        lenght = 0
        result = []
        while curr:
            curr = curr.next
            lenght+=1
        parts , rem = divmod(lenght , k)
        curr = head
        for i in range(k):
            root_temp = temp = ListNode(None)
            for j in range(parts + (i < rem)):
                temp.next = temp = ListNode(curr.val)
                #each time we want to make temp points to last possible value that our part
                #should end
                if curr: 
                    curr = curr.next
            result.append(root_temp.next) #Since it starting point is None 
        return result 
                    