class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lists = nums.copy()
        nums.sort()
        map_ = {}
        result = []
        for i in range(len(nums)-1 , -1 , -1):
            counter = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    counter+=1
            result.append(counter)
            map_[nums[i]] = counter
        for i in range(len(lists)):
            for keys , values in map_.items():
                if keys == lists[i]:
                    result[i] = values
                    
        return result 
                    