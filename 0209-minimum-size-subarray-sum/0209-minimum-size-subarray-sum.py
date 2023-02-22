class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        max_ = 0
        l  , r = 0 , 0
        min_ = float('inf')
        summed = 0
        for r in range(len(nums)):
            summed+=nums[r]
            while summed >= target:
                min_ = min(min_ , r-l+1)
                summed-=nums[l]
                l+=1
                
        return min_  if sum(nums) >= target else 0
                