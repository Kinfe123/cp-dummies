class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dp = defaultdict(int)
        result = []
        
        for i in range(len(arr)):
            if arr[i] - diff not in dp:
                dp[arr[i]] = 1
                count = 0
            else:
                count = dp[arr[i] - diff]
            dp[arr[i]] = (count + 1)
            result.append(dp[arr[i]])
            
            
        return max(result)
#             if indx >= len(arr):
#                 return 1
#             if indx == len(arr)-1:
#                 return 
#             if (indx , connt) in dp:
#                 return dp[(indx , count)
#             dp[(indx , count)] = 1 + solve(indx + diff)
#             return dp[indx]
            
        
   
        
        
        
        
        