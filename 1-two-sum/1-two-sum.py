class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        for i in range(len(nums)):
            
            rem = k - nums[i]
            if rem in dic:
                return [dic[rem] , i]
            else:
                dic[nums[i]] = i
