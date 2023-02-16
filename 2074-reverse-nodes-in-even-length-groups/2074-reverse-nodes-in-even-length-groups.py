# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        lenght = 0
        lists = []
        while temp:
            lists.append(temp.val)
            temp = temp.next
            lenght+=1
        i1 , i2 = 0 , 0
        start , end = 0 , 0
        result = []
        while end -i2 <= lenght:
            
            result.append(lists[start:end+1])
            i2+=1
            start+=i2
            end+=(i2+1)
        result = [i for i in result if i != []]
        rev = True
        for i in result:
            if len(i) % 2 == 0:
                i.reverse()
            
        dummy = curr = ListNode()
        for i in result:
            for j in i:
                curr.next = ListNode(j)
                curr = curr.next
        curr.next = None
        return dummy.next
            
        
        