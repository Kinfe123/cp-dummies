class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        # nums.sort()
        map_ = defaultdict(int)
        for i in range(len(nums)):
            if target == nums[i]:
                result.append(i)
                map_[i] = nums[i]
                
        
        if not map_:
            return [-1 , -1]
        else:
            return [list(map_.keys())[0] , list(map_.keys())[-1]]

       
                
        # if len(result) == 2:
        #     return result
        # elif len(result) == 1:
        #     result.append(result[0])
        #     return result
        # else:
        #     return [-1 , -1]
        
                    
        