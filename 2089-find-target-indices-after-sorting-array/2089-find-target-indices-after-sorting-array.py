class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if target == nums[i]:
                result.append(i)
        result.sort()
        return result
                
        