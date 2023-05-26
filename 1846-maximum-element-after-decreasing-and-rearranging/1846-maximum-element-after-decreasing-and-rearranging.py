class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        
        
       
   
        arr.sort()
        lists = list(range(1 , len(arr)+1))
        res = 1
        arr[0] = 1
      
        for i in range(len(arr)):
            res = min(res+1 , arr[i])
            lists[i] = min(lists[i] , arr[i])
        return res

     
                    
                   