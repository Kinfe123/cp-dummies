class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort() 
        left , right = 0 , 0
        total = 0
        res = 0
        #right poiter is less than the lenght of nums
        while right < len(nums):
            total+=nums[right]
            #right-left + 1 is a window lenght 
            while nums[right]*(right-left+1) > total + k:
                total-=nums[left]
                left+=1
            res = max(res , right-left+1)
            right+=1
        return res
        
            
                
            
                
        