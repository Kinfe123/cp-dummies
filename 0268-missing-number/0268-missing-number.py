class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append('x')
        for i in range(len(nums)):
            while nums[i] != 'x' and nums[i] != i:
                temp = nums[i]
                nums[i] , nums[temp] = nums[temp] , nums[i]
        for i in range(len(nums)):
            if nums[i] == "x":
                return i
            
                
            
        