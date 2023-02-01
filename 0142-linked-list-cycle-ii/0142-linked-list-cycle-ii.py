# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        set_h = set()
        lists = []
        temp = head 
        while temp:
            if temp in set_h:
                return lists[lists.index(temp)]
            else:
                
                set_h.add(temp)
                lists.append(temp)
            temp = temp.next
        return None