# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getTheKth(self, nodes , k):
        while nodes and k > 0:
            nodes = nodes.next
            k-=1
        return nodes
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        dummy = ListNode()
        dummy.next = head
        prevOnes = dummy
        #NOw dummy and previous one is pointing to the same head 
        
        
        #Start catching the end of the group and reversing the group 
        while True:
            endOfGroup = self.getTheKth(prevOnes , k)
            if not endOfGroup:
                break
            nextOnes = endOfGroup.next
            current , previous = prevOnes.next , endOfGroup.next
            while current != nextOnes:
                saver = current.next
                current.next = previous
                previous = current 
                current = saver 
            tempSaver = prevOnes.next
            
            prevOnes.next = endOfGroup
            
            #we should have to make the very first and the end of the group in a correct position
            #Like pointing the changing the pointer of the first and last element of the groups 
            prevOnes = tempSaver
            
        return dummy.next
            
                
        
        
