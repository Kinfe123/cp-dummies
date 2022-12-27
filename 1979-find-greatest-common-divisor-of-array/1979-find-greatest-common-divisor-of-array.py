from math import gcd

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return gcd(nums[0] , nums[-1])
        
        