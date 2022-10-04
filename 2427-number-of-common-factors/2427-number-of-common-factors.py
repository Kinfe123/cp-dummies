class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        counter = 0
        for i in range(1 ,a):
            
            if a % i == 0 and b % i == 0:
                counter +=1
        return counter if a!=b else counter+1
        