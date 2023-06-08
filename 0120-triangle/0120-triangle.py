class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = defaultdict(int)
        def dp(indx , inner):
            if indx == len(triangle):
                return 0
            if inner == len(triangle[indx]):
                return 0
            
            
            
            if (indx , inner) in memo:
                return memo[(indx , inner)]
            memo[(indx , inner)] = min(dp(indx + 1 , inner) + triangle[indx][inner] , dp(indx +1 , inner+1) + triangle[indx][inner])
            
            return memo[(indx , inner)]
        return dp(0 , 0)
            
        
