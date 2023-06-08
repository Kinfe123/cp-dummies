class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
    
       
       
        def dp( sum_):
            if sum_ == target:
                return 1
            if sum_ > target:
                return 0
            
            if sum_ in memo:
                return memo[sum_]
            
            temp = 0
            for i in nums:
                if sum_ + i <= target:
                    memo[sum_] += (dp( sum_ + i))
                
                    
                
            return memo[sum_]
            
        # print(memo)
            
            
        return dp( 0)
    