class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for key , value in Counter(nums).items():
            if value >= 2:
                return key
        