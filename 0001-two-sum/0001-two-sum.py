class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        map_ = defaultdict(int)
        for i in range(len(nums)):
            looking_for = target - nums[i]
            if nums[i] in map_:
                return [map_[nums[i]] ,  i]
            else:
                map_[looking_for] = i
                
        return [-1 , -1]
                
            
        
                    