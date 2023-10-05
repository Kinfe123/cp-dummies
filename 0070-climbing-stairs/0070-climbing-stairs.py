class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+2)
        dp[0] = 0
        dp[1] = 1
        for i in range(2 , n+2):
            dp[i] = dp[i-2] + dp[i-1]
        print(dp)
        return dp[-1]
        