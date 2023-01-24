class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_ = 0
        lists = []
        for i in range(1, len(nums) , 2):
            max_ += min(nums[i] , nums[i-1])
        return max_
            
            
                
                    
        