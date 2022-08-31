class Solution(object):
    def findKthBit(self, n, k):
        
        if k == 1:
            return(str(0))
        else:
            
        
             arr = [0]
             arr2 = [1]
             while k > len(arr):
                templast = arr
                temp2last = arr2
                arr = templast + [1] + temp2last
                arr2 = templast + [0] + temp2last
             return(str(arr[k-1]))

        