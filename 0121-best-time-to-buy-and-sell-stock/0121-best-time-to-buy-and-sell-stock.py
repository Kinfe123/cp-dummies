class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        diff = 0
        least = float('inf')
        for i in range(len(prices)):
            if least > prices[i]:
                least = prices[i]
            diff = prices[i] - least
            if diff > profit:
                profit = diff
        return profit
       