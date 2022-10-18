class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product , current , l= 1 , 0 , 0
        
        for r in range(len(nums)):
            product*=nums[r]
            while product >= k and l<=r:
                product/=nums[l]
                l+=1
            current+= r-l+1
        return current 
            