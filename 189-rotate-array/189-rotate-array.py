class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        
        def rev(l=0, r=len(nums) - 1):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r -1
        rev()    
        rev(r=k-1)
        rev(l=k)