class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = defaultdict(int)
        res = []
        
        for i in range(len(nums)):
            
            if nums[i] in map_:
                res = [map_[nums[i]] , i]
                # return [i , map_[target - nums[i]]]
                break
            
            
            map_[target-nums[i]] = i
            # print('THe mapped ; ', map_)
        return res
        