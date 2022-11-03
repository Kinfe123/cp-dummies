class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = l = 0
        summed = 0
        result = 0
        for right , value in enumerate(nums):
            summed+=value
            if value==1:
                counter = 0
                #Because the value will be changed so we should have to restart out counter
                
            while l <= right and summed >= goal:
                if summed == goal:
                    counter+=1
                summed -= nums[l]
                l+=1
            result+=counter
        return result 