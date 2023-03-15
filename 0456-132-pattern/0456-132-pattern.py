class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        isTrue = False
        second = float('-inf')
        for i in range(len(nums)-1 , -1 , -1):
            if second > nums[i]:
                #finding the second largest element in 132 pattern
            
                return True 
            while stack and stack[-1] < nums[i]:
                #every time when we pop the element we should have to update
                #and make it as min since we are building a decreasing mono
                #stack
                second = stack.pop()

            stack.append(nums[i])
        return False
        