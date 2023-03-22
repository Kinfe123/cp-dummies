class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
     
        def backtrackish(nums, path=[]):
            
        
            if not nums: 
                result.append(path) 
                #till we have left with no elements left  

            for i in range(len(nums)): 
       
                
               
                backtrackish(nums[:i] + nums[i+1:], path+[nums[i]]) 
                
                
       
        
        backtrackish(nums , path=[])
        return result
                
            
        