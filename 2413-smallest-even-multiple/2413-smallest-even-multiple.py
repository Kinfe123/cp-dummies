class Solution:
    def smallestEvenMultiple(self, num: int) -> int:
        result = num*2
        for i in range(1 , num):
            result = num*i
            if result % 2 == 0:
                return result 
            else:
                pass
        return result