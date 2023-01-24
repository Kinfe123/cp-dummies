
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        summed = sum(cost)
        if len(cost) == 2:
            return sum(cost)
        i = len(cost)-3
        
        summed = sum(cost)
        while i >= 0:
            summed-=cost[i]
            i-=3
            
      
        return summed
            
            
#         for i in range(len(cost)-1 , 1, -2):
#             bought.append(cost[i-1])
#             bought.append(cost[i])
            
#             min_ = min(cost[i] , cost[i-1])
#             if min_ <= cost[i-2]:
#                 free.append(cost[i-2])
                

    
     
            
            
        