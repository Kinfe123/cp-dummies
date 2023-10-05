class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pos = []
        map_ = defaultdict(int)
        zipped = [(x , y) for x , y in zip(ages , scores)]
        zipped.sort()
        
#         for i in range(len(scores)):
#             for j in range(i+1 , len(ages)):
#                 if ages[i] >= ages[j]:
                    
#                     scores[i] , scores[j] = scores[j] , scores[i]
#                     ages[i] , ages[j] = ages[j] , ages[i]
                    
#         def dp(indx, summation):
#             if indx >= len(scores):
#                 return 0
            
#             if 
            
            
        # return dp(0 , 0)
        # process = []
        # print(scores , sum(scores))
        res = []
        @cache
        def dp( indx  ):
            if indx < 0:
                return 0
            curr_ = 1
            summ = scores[indx]
            
            for i in range(indx - 1 , -1 , -1):
                if ages[indx] >= ages[i]:
                    # summ +=nums[i]
                
                    
                    summ = max(summ , scores[indx] + dp(i))
                    
            
                    
                    
           
            return summ 
            
        dp = [s for _ , s in zipped]
        scores = dp[:]
        for i in range(len(scores)):
            mx = 0
            for j in range(i):
                if scores[i] >= scores[j]:
                    mx = max(mx , dp[j])
            dp[i]+=mx
        print(dp , scores)
        return max(dp)
                    
        
                
        
                
        
                    
        