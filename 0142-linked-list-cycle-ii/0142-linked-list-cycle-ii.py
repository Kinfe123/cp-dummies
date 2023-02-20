# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        map_ = {}
        temp = head 
        count = 0
        while temp:
            if temp in map_:
                return temp 
            
            map_[temp] = count 
            temp = temp.next
            count+=1
        return None
            
        # slow = head
        # fast = head.next
        # while fast and fast.next:
        #     if slow == fast.next:
        #         return slow
        #     fast = fast.next.next
        #     slow = slow.next
        # return None