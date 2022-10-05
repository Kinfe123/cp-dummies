class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        max_sum = current_max
        for i in range(1 , len(nums)):
            current_max = max(current_max + nums[i] , nums[i])
            max_sum = max(current_max , max_sum)
        return max_sum