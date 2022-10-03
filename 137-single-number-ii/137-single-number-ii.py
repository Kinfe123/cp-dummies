class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for keys , values in Counter(nums).items():
            if values == 1:
                return keys
        