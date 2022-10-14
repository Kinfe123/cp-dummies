class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        base_ = len(nums) / 2
        values = Counter(nums)
        for keys , value in values.items():
            if value > base_:
                return keys 