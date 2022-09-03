class Solution(object):
    def converter(self , value):
        res = ""
        for i in range(len(value)-1 , -1 , -1):
            res+=value[i]
        return res
    def reverse(self, nums):
        """
        :type x: int
        :rtype: int
        """
        result = 0
       
        if nums > 0:
            conv = str(nums)
            result = int(self.converter(conv))
            return result if result >= -2**31 and result <= 2**31-1 else 0
        else:
            abso = abs(nums)
            conv = str(abso)
            modify = "-" + self.converter(conv)
            result = int(modify)
            return result if result >= -2**31 and result <= 2**31-1 else 0
    
        
        