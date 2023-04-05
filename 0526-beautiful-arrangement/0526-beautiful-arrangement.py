class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n+1)]
        res = 0
        def backtrack(nums , index ):
            
            if index == len(nums):
                #since we are pruning , we can be sure that we will get the valid answer
                return 1
            
            res = 0
            for i in range(index , len(nums)):
                nums[i] , nums[index] = nums[index] ,nums[i]
                if nums[index] % (index+1) == 0 or (index + 1)%nums[index]==0:
                    res += backtrack(nums , index+1)
                    
                nums[i] , nums[index] = nums[index] ,nums[i]
            return res
       
        return backtrack(nums  , 0)
                    
            
        