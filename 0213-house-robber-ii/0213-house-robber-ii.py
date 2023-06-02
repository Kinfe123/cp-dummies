class Solution:
    def rob(self, nums: List[int]) -> int:
        max_ = 0
        cached_ = defaultdict(int)
        if len(nums)==1:
            return nums[0]
            
        # nums.extend(nums)
        def dp(curr):
            # curr = curr % len(nums)
            nonlocal max_
            nonlocal cached_
           
            # max_ = max(max_ , sum_)
           
            if curr < 0:
                
                return 0
            if curr in cached_:
                return cached_[curr]
            # if curr == dest-1:
            #     return nums[curr]
            # if curr == dest-1:
            #     return nums[curr]
            
            else:
                if curr not in cached_:
                
                    cached_[curr] = max(dp(curr - 1 )  , dp(curr - 2 )+nums[curr])
                    
                return cached_[curr]
            
            
                # cached_[curr] = max_
                
        op1 = dp(len(nums)-2)
        cached_ = defaultdict(int)
        nums.pop(0)
        op2 = dp(len(nums)-1)
        
        return max(op1 , op2)
        # return max_
           
            
                
                
            
                
            
            
            
            
            
            
        