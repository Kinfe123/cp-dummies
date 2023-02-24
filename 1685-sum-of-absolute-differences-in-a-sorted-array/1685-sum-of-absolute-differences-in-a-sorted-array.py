class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix , summed  , res = [0] , 0 , []
        n = len(nums)
        for num in nums:
            prefix += [num + prefix[-1]]
        
        for i , num in enumerate(nums):
            result =  i * num - prefix[i] + prefix[n] - prefix[i] - (n - i) * num
            res.append(result)
            
          
        return res
            
            
        
        