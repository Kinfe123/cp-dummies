class Solution:
    
    # search for duplicate numbers
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # number of good pairs
        # we can use combination formula for finding the solution
        num = 0
        repeat = {}
        for i in nums:
            if i in repeat:
                if repeat[i] == 1:
                    num+=1
                else:
                    num+=repeat[i]
                repeat[i] += 1
            else:
                repeat[i] = 1
                
        return num
                
                
                
        
                 
                
            