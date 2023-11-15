class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = max(curr_sum + nums[i] , nums[i])
            max_sum = max(max_sum , curr_sum)
        return max_sum
            #you do stuff here in one line
        