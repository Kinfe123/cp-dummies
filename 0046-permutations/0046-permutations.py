class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result , current = [] , []
        # state_ = 0
        def backtrackish(index , state_):
            if index == len(nums):
                result.append(current.copy())
                return 
            
            for i in range(len(nums)):
                # if it is not been permutated 
                if state_ & (1 << i) == 0:
                    #we will include to  be permutated 
                    #by setting it on for the next iter
                    state_ |= (1 << i)
                    current.append(nums[i] )
                  
                    backtrackish(index+1 , state_)  
                    
                    
                    current.pop()
                    # we will do some clean up and finding another way to permutate the numbers
                    state_ ^= (1 << i)
                    
        backtrackish(0 , 0)
        return result
            
            
            
            
            