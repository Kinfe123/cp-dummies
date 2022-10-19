class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        map_ = {}
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum == k:
                count+=1
            if curr_sum - k in map_:
                count+=map_[curr_sum-k]
            if curr_sum in map_:
                map_[curr_sum] += 1
            else:
                map_[curr_sum] = 1
        return count 
                
            