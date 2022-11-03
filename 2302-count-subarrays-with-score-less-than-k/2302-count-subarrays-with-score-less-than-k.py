class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        counter  , l , answer = 0 , 0 , 0
        summ = 0
        for i in range(len(nums)):
            summ+=nums[i]
            while summ * (i-l+1) >= k:
                summ-=nums[l]
                l+=1
            answer+=i-l+1
            
        return answer
            
        
            