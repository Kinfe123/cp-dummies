class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_ = 0
        costs = sorted(costs , key=lambda x: x[0] - x[1])
       
        l , r = 0 , len(costs)-1
        while l <= r:
            min_+=costs[l][0]
            min_+=costs[r][1]
            l+=1
            r-=1
        return min_

    