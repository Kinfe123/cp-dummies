class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summed = 0
        for i in range(len(nums)):
            summed+=nums[i]
            nums[i] = summed
        return nums