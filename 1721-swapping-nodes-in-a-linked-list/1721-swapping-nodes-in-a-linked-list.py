# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lists = []
        
        temp = head
        while temp:
            lists.append(temp.val)
            temp = temp.next
        end = len(lists)-1
        start = 0
        for i in range(len(lists)):
            if i - start == k-1:
                lists[i] , lists[end-i] = lists[end-i] , lists[i]

                
        print(lists)
        dummy = curr = ListNode()
        
     
        while start <= end:
            curr.next = ListNode(lists[start])
            start+=1
            curr = curr.next
        curr.next = None
        return dummy.next
            
        
            
            
            
        