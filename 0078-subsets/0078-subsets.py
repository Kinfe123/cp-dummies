class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def dfsBackTrack(index):
            if index >= len(nums):
                result.append(current.copy())
                return 
            
            
            #including on the decision tree 
            current.append(nums[index])
            dfsBackTrack(index+1)
            
            
            #Not including 
            current.pop()
            #for not including we will be calculating the including and not
            #including decision tree
            dfsBackTrack(index+1)
            
        dfsBackTrack(0)
        return result
            
        
        