class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map_ = {}
        curr = 0
        count = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr == k:
                count+=1
            if curr - k in map_:
                count+=map_[curr - k]
            if curr in map_:
                map_[curr] += 1
            else:
                map_[curr] = 1
        return count
                
        