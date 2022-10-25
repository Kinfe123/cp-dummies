class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 2:
            return nums.reverse()
        pointer = length - 2
        while pointer >= 0 and nums[pointer] >= nums[pointer+1]:
            pointer-=1
        if pointer == -1:
            return nums.reverse()
        for i in range(length-1 , pointer , -1):
            if nums[i] > nums[pointer]:
                nums[i] , nums[pointer] = nums[pointer] , nums[i]
                break
        nums[pointer+1:] = reversed(nums[pointer+1:])
        return nums
            
            
        