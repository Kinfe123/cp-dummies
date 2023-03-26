class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        bisected = []
        for i in range(len(queries)):
            bisected.append(bisect.bisect_left(nums , queries[i]))
        summed = sum(nums)
        prefix = [0] + list(accumulate(nums))
      
        result = []
        l , r = 0 , len(nums)-1
        ans = 0
        
        for i in range(len(bisected)):
            
            # print( prefix[bisected[i]-1])
      
            ans = ((queries[i] * bisected[i] ) - prefix[bisected[i]]) + (prefix[n] - prefix[bisected[i]] - queries[i] * (n - bisected[i]))
         
          
                
                
            result.append(ans)
        
            
        
               
                  
        return result 
            
            
        