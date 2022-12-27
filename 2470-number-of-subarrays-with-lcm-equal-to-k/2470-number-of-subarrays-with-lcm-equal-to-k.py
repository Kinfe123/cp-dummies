from math import gcd
class Solution:
    def LCM(self , a , b):
        
        return abs(a*b)//math.gcd(a , b)
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            currentLCM = nums[i]
            for j in range(i , n):
                currentLCM = self.LCM(currentLCM , nums[j])
                #The key point is keeping track of the previous lcm that we had and
                #try to make a lcm out of it with in the lcm function
                # print(currentLCM)
                if currentLCM == k:
                    count+=1
                else:
                    pass
        return count
                    
            
            
        