class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        lists = [i for i in range(1 ,len(nums) + 1)]
        n = len(nums)
        nums.sort()

        duplicated_ = 0
        #duplication handling phase
        for i in range(1, len(nums)):
            if nums[i] ^ nums[i-1] == 0:
                duplicated_ = nums[i]
                break
        
                
        #Missing number finding phase
        nums = list(set(nums))
        total = len(nums)+1 
        missed = 0
      
        for i in range(len(nums)):
            total ^= nums[i]
            missed^= i
        missed ^= len(nums)
        missed = total ^ missed
        #merging the missing and duplicates together  
        return [duplicated_ , missed] 
            
        