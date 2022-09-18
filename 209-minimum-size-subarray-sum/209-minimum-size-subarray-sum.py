class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        left , currSum = 0 , 0 
        res = float('inf')
        for right in range(len(nums)):
            currSum+=nums[right]
            while currSum >= k:
                res = min(res , right - left + 1)
                currSum-=nums[left]
                left+=1
                
            
        return 0 if res == float('inf') else res
        