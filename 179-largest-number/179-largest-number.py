import itertools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for index , value in enumerate(nums):
            nums[index] = str(value)
        def cmp(a , b):
            if a + b > b + a:
                return -1 
            else:
                return 1
        nums = sorted(nums , key=cmp_to_key(cmp))
        
        return str(int("".join(nums)))