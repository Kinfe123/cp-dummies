class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for a in range(n):
            for b in range(a+1,n): # starts at a+1 so as to not repeat the same number multiple times
                for c in range(b+1,n):
                    for d in range(c+1,n):
                        count += nums[a]+nums[b]+nums[c] == nums[d] #adds 0 if the statement is false and 1 if true
        return count