class Solution:
    def rob(self, nums: List[int]) -> int:
        max_ = 0
        cached_ = defaultdict(int)
        def dp(curr ):
            nonlocal max_
            
            # max_ = max(max_ , sum_)
            if curr == len(nums):
                return 0
            if curr == len(nums)-1:
                return nums[curr]
            else:
                if curr not in cached_:
                
                    cached_[curr] = max(dp(curr + 1)  , dp(curr + 2)+nums[curr])
                    
                return cached_[curr]
                # cached_[curr] = max_
        return dp(0 )
        # return max_
           
            
                
                
            
                
            
            
            
            
            
            
        