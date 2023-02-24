class Solution:
    def trap(self, lists: List[int]) -> int:
        

        max_r = [0] * len(lists)
        max_l = [0]  * len(lists)

        for i in range(len(lists)):
            max_r[i] = max(max_r[i-1] , lists[i])
        for i in range(len(lists)-2 , -1 , -1):

            max_l[i] = max(max_l[i+1] , lists[i+1])
        result = 0
        for i in range(len(lists)):
            answer = min(max_l[i] , max_r[i]) - lists[i]
            if answer >= 0:
                result+=answer
        return result 

