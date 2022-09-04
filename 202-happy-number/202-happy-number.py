class Solution(object):
    def change(self , n):
        if n == 1:
            return 1
        con = str(n)
        lists = [int(i) for i in con]
        squares = 0
        for i in lists:
            squares += i**2
        return squares

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        n = self.change(n)
        isHappy = False
        res = n
        while n!=1 and n!=4:
            n = self.change(n)
        if n == 1:
            isHappy = True 
        else:
            isHappy = False

            
        return isHappy

        
        