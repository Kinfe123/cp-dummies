class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroFinder = 0
        # nonZeroFinder = 0
        for nonZeroFinder in range(len(nums)):
            if nums[zeroFinder] == 0 and nums[nonZeroFinder] != 0:
                nums[zeroFinder] , nums[nonZeroFinder] = nums[nonZeroFinder] , nums[zeroFinder]
            if nums[zeroFinder] != 0:
                zeroFinder+=1
        return nums
                
        