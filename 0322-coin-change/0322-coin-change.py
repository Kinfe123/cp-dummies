class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (10**4+1)
        dp[0] = 0
        for i in range(1 , amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i] , dp[i - coin] + 1) 
        # print(dp)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
        