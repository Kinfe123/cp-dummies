class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        i = 0
        stack = []
        while i < 2 * len(nums):
            while stack and nums[i % len(nums)] > nums[stack[-1]]:
                
                result[stack[-1]] = nums[i%len(nums)]
                stack.pop()
            stack.append(i%len(nums))
            i+=1
        
        return result
                
        