class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currentSum = 0
        map_ = {}
        for i in range(len(nums)):
            currentSum+=nums[i]
            if currentSum == k:
                count+=1
            if currentSum-k in map_:
                count+=map_[currentSum - k]
            if currentSum in map_:
                map_[currentSum] += 1
            else:
                map_[currentSum] = 1
        return count
       