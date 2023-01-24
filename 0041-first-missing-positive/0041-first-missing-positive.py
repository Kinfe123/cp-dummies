class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        looksup = set(nums)
        for i in range(1 , len(nums)+1):
            if i not in looksup:
                return i
        return len(nums)+1
        