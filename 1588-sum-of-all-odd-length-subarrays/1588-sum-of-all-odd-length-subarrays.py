class Solution:
    def sumOddLengthSubarrays(self, nums: List[int]) -> int:
        start = 0 
        end = 0
        summed = 0
        for i in range(len(nums)):

            while start != len(nums):
                subs = nums[start:end+1]
                end+=1
                if end == len(nums):
                    end = start+1
                    start +=1

                if len(subs) % 2 != 0:
                    summed+=sum(subs)
                else:
                    pass

        return summed
