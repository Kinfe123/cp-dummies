class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        map_ = {}
        max_ = 0
        summed = 0
        elements = set()
        for r in range(len(nums)):
            summed+=nums[r]
            if nums[r] not in map_:
                map_[nums[r]] = 1
            else:
                map_[nums[r]] += 1
            while map_[nums[r]] > 1:
                summed-=nums[l]
                
                map_[nums[l]]-=1
                l+=1
            else:
                max_ = max(max_ , summed)
        return max_
                
            
                
                
                
            
                

        