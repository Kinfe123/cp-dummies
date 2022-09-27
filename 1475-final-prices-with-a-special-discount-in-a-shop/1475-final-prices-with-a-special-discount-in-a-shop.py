class Solution:
    def finalPrices(self, nums: List[int]) -> List[int]:
        stack = []

        for i , v in enumerate(nums):
            while stack and nums[stack[-1]] >= v:
                nums[stack.pop()]-=v
            stack.append(i)
        return nums

     