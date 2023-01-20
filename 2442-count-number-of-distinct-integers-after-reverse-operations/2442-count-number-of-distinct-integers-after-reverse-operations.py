class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        lists = [int(str(i)[::-1]) for i in nums]
        nums = nums + lists
        return len(set(nums))
        