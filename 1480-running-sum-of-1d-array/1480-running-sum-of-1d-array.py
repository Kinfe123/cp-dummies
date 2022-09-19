class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currSum = 0
        for i in range(len(nums)):
            currSum+=nums[i]
            nums[i] = currSum
        return nums