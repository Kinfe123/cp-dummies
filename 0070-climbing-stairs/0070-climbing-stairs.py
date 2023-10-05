class Solution:
    def climbStairs(self, n: int) -> int:
        dps = [0] * (n+1)
        def dp(indx):
            if indx ==0 or indx == 1:
                return 1
            if dps[indx]:
                return dps[indx]
            dps[indx] = dp(indx-1) + dp(indx-2)
            
            return dps[indx]
        return dp(n)
        