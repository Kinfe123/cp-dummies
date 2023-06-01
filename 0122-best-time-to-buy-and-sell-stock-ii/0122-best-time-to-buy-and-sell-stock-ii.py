class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(int)
        
        def transact(indx , can):
            if indx == len(prices):
                return 0
            if (indx , can) in dp:
                return dp[(indx ,can)]            
            
            
            op1 = transact(indx + 1 , can)
            
            if can:
                op2 = -prices[indx] + transact(indx+1 , False)
            else:
                op2 = prices[indx]  + transact(indx+1 , True)  
            dp[(indx , can )] = max(op1 , op2)
            return dp[(indx , can)]
            
        
        
        
        
        return transact(0 , True)