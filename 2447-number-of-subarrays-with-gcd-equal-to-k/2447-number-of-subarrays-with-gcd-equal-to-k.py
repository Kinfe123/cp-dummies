from math import gcd

class Solution:
    
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            currentGCD = nums[i]
            for j in range(i , n):
                currentGCD = gcd(currentGCD , nums[j])
                if currentGCD == k:
                    count+=1
        return count 