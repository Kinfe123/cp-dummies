class Solution:
    def getDescentPeriods(self, nums: List[int]) -> int:
        count = 1
        start = 0
        end = 0
        for i in range(1 , len(nums)):
            if nums[i] == nums[i-1] -1:
                count+=i-start+1
            else:
                start = i 
                count+=i-start+1

        return count 