class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        map_ = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if curr_sum == k:
                count+=1
            if curr_sum - k in map_:
                count+=map_[curr_sum - k]
            if curr_sum in map_:
                map_[curr_sum] += 1
            else:
                map_[curr_sum] = 1
        return count 

                