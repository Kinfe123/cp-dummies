class Solution:
    def numDecodings(self, s: str) -> int:
        
        ways_ = 0
        memo = defaultdict(int)
        
#         dp = [0] * (len(s) + 1)
#         if dp[0] != '0':
#             dp[0] = 1
#         for i in range(2 , len(s)+1):
#             if s[i-1] != '0':
#                 dp[i] += dp[i-1]
#             if '10' <= s[i-2: i] <= '26':
#                 dp[i] += dp[i-2]
#         return dp[len(s)]
                
                
            
                
        def dp(indx):
            if indx == len(s):
                return 1
          
            
            if indx in memo:
                return memo[indx]
            # if s[indx] != '0':
            #     return 1
           
            if indx <= len(s)-1 and s[indx] != '0':
                memo[indx] += (dp(indx + 1))
            if '10' <= s[indx : indx  + 2] <= '26':
                memo[indx] += (dp(indx + 2))
            return memo[indx]
    
            
            
        
        
        return dp(0)
        
        