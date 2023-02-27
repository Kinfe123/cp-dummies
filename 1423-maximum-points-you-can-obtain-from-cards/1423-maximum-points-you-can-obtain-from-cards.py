class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #the sliding window technique will be used for solving this problem
        #with the size of n - k
        l , r = 0 , 1
        n = len(cardPoints)
        if k>=n:
            return sum(cardPoints)
        total = 0
        min_ = float('inf')
        cardPoints.append(0)
        for r in range(n+1):
            if r - l == n-k:
                print(total)
                min_ = min(min_ , total )
                total-=cardPoints[l]
                l+=1
            total+=cardPoints[r]
      
        return sum(cardPoints) - min_
                
                
            
            
            
        
        