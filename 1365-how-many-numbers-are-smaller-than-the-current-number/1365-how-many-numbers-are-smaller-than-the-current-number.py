class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lists= sorted(nums)
        map_ = {}
        ans = []
        for i in range(len(lists)):
            if lists[i] not in map_:
                map_[lists[i]] = i
        for i in range(len(nums)):
            ans.append(map_[nums[i]])
        return ans
            
            
        
  
                    