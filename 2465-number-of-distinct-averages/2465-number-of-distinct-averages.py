class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        set_ = set()
        l , r = 0 , len(nums)-1
        nums.sort()
        while l <= r:
            mean = (nums[r] + nums[l])/2
            set_.add(mean)
            l+=1
            r-=1
        return len(set_)
            
        