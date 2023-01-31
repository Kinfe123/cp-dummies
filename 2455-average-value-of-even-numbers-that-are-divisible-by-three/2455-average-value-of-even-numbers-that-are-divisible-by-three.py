class Solution:
    def averageValue(self, nums: List[int]) -> int:
    
        stack = []
        for i in range(len(nums)):
            if nums[i] % 6 == 0:
                stack.append(nums[i])
        return sum(stack)//len(stack) if len(stack) > 0 else 0
        