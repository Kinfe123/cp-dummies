import sys
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        counter = Counter()
        curr_sum = 0
        max_ = 0
        # print(max_)
        l = 0
        for r in range(len(nums)):
            counter[nums[r]]+=1
            curr_sum+=nums[r]
            while r-l+1 > k or counter[nums[r]] > 1:
                counter[nums[l]]-=1
                curr_sum-=nums[l]
                l+=1

            if r-l+1 == k:
                max_ = max(curr_sum , max_)
        return max_

        