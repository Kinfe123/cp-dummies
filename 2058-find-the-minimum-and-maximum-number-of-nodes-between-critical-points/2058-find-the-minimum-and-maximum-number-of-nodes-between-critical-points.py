# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        lenght = 0
        temp = head
        result = []
        # while temp:
        #     temp = temp.next
        #     lenght+=1
        # if lenght < 3:
        #     return [-1 , -1]
        temp2 = head
        map_ = {}
        prev_curr , curr , next_curr = temp2 , temp2.next , temp2.next.next
        pos = 1
        while next_curr:
            #Local maxima
            if curr.val > prev_curr.val and curr.val > next_curr.val:
                map_[pos] = curr.val
                print('the local maxima: ' , curr.val)
            elif curr.val < prev_curr.val and curr.val < next_curr.val:
                map_[pos] = curr.val
                print('the local minima; ' , curr.val)
            prev_curr = curr
            pos+=1
            curr = next_curr
            next_curr = next_curr.next
        if len(map_) < 2:
            return [-1 , -1]
        lists1 = list(map_.keys())
        max_ = lists1[-1] - lists1[0]
        min_ = float('inf')
        for i in range(1 , len(lists1)):
            min_ = min(lists1[i] - lists1[i-1] , min_)
        return [min_ , max_]
            
        
            
            
            
            
        