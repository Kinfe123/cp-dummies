class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        map_ = {}
        for i in nums:
            if i  in map_:
                map_[i]+=1
            else:
                map_[i] = 1

        return [keys for keys , values in map_.items() if values==2]
                
            
        