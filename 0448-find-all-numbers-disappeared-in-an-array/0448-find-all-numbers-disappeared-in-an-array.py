class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # if len(nums) <= 2:
        #     if nums[0] == nums[-1]:
        #         return [nums[-1] + 1 if nums[-1] <= 1 else nums[-1] - 1]
        notFound = [i for i in range(1  , len(nums)+1)]
        return set(notFound) - set(nums)
       
        