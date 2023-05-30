class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = 0
        res = []
        if amount == 0:
            return 0
        if amount in set(coins):
            return 1
        
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = [0]
        @lru_cache(None)
        def collect(x):
            if x == 0:
                return x
            #for other paths
            res = float('inf')
            for i in range(len(coins)):
                if x >= coins[i]:
                    
                    res = min(res , 1+collect(x-coins[i]))
            return res
        
        val = collect(amount) 
        if val == float('inf'):
            return -1
        
        return val
            
         