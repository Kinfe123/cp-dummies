class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isOk(mid):
            total = 0
            count = 1# since we have started from the max we can ship at least 
            
            for i in range(len(weights)):
                total += weights[i]
                if total > mid:
                    count += 1
                    total = weights[i]
                
                
            
            return count
                    
                    
        low , high = max(weights) , sum(weights)

        #since we are not returning any thing we will be looking for the least
        # weight as possible 
        while low < high:
            mid = low + (high-low)//2
            if isOk(mid) <= days:
                #it can be shipped and mid might be the left most answer
                # so we dont need to mid - 1 
                # anything to the right of high will not be used : least
                high = mid
            else:
                #anything mid and left of mid doesnt work
                low = mid + 1
        return high
                
            
                
        