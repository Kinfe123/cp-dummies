class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        result = False
        while n > 0:
            m = n % 2
            if m == 0:
                n = n / 2
                if n == 1:
                    return True 
            else:
                return False
        return False
               