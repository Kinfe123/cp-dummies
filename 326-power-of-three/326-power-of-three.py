class Solution(object):
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        result = False
        while n > 0:
            m = n % 3
            if m == 0:
                n = n /3 
                if n == 1:
                    return True 
            else:
                return False
        return False
    
    
                
        
        
    
        