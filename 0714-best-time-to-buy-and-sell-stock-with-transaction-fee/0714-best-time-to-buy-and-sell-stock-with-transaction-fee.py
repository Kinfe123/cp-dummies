class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp = defaultdict(int)
        @cache
        def transact(indx , can):
            if indx == len(prices):
                return 0
            
            
            
            op1 = transact(indx + 1 , can)
            
            if can:
                op2 = -prices[indx] + transact(indx+1 , False)
            else:
                op2 = prices[indx] - fee + transact(indx+1 , True)

            return max(op1, op2)
            
        
        
        
        
        return transact(0 , True)