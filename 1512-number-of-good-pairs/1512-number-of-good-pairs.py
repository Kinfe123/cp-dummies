class Solution:
    
    # search for duplicate numbers
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # number of good pairs
        # we can use combination formula for finding the solution
        num = 0
        dict_ = {}
        summed = 0
        for i in range(len(nums)):
            if nums[i] in dict_:
                dict_[nums[i]]+=1
            else:
                dict_[nums[i]] = 1
                
        for keys , values in dict_.items():
            if values > 1:
                summed+= (0.5*values) * (values-1)
        return int(summed)
        
        
            
                
        print(dict_)
                
                
                
        
                 
                
            