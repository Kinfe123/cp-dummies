
class Solution:
    
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        
        prefix = 1
        postfix = 1
        output = [1] * len(arr)
        for i in range(len(arr)):
            output[i] = prefix
            prefix*=arr[i]
        for i in range(len(arr)-1 , -1 , -1 ):
            output[i] *= postfix
            postfix *= arr[i]
        return output 
            
        
        