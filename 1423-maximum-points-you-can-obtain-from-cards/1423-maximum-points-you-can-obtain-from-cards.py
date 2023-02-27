class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #the sliding window technique will be used for solving this problem
        #with the size of n - k
        n = len(cardPoints)
        l , r = 0 , n-k
        summed = sum(cardPoints[r:])
        max_result = summed 
        while r < n:
            summed-=cardPoints[r]
            summed+=cardPoints[l]
            max_result = max(max_result , summed)
            l+=1
            r+=1
        return max_result 
    
                
            
            
            
        
        