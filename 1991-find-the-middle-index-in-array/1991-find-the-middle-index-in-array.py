class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        rightTotal = sum(nums)
        leftTotal = 0
        for index , value in enumerate(nums):
            rightTotal-=value
            if leftTotal == rightTotal:
                return index
            leftTotal+=value
            
        return -1
        