class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        map_ = {}
        
        for i in range(len(nums)):
            curr_sum+=nums[i]
            curr_sum %= k
            if curr_sum == 0:
                count+=1
            if curr_sum  in map_:
                count+=map_[curr_sum]
            if curr_sum in map_:
                map_[curr_sum] += 1
            else:
                map_[curr_sum] = 1
        return count