class Solution(object):
    def isPowerOfFour(self, n):
        if n == 1:
            return True
        result = False
        while n > 0:
            m = n % 4
            if m == 0:
                n = n /4 
                if n == 1:
                    return True 
            else:
                return False
        return False
    
    
        