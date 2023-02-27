class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        counters = 0
    
        l  , r = 0, len(nums)//2
        
        
        while r < len(nums) and l < len(nums)//2:
            if l <= r and nums[l] * 2 <= nums[r]:
                l+=1
            r+=1
            
     
        return l*2
            
                
                
            
            
        
        