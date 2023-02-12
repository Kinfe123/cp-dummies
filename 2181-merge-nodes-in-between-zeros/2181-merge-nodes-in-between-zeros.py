# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        temp = temp.next
        summed = 0
        seeker = head 
        
        '''
        I'm just overwriting the value of the head nodes with the sum that i have found so far and after we have exhausted finding zero , we will be making our seeker next to be None 
        
        '''
        while temp:
            if temp.val == 0:
                seeker = seeker.next
                #This is due to the zero issue 
                seeker.val = summed
                summed = 0
            else:
                summed += temp.val 
            temp = temp.next
        seeker.next = None
        
        #Again due to zero issue 
        return head.next 
    
