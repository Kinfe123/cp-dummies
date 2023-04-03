class Solution:
    def calc(self , lists):
        pro = 1
        for i in lists:
            pro*=i
        return pro
    def is_prime(self , num):
    
        if num == 0 or num == 1:
            return False
        for x in range(2, num):
            if num % x == 0:
                return False
        else:
            return True
        
# lists = list(filter(is_prime, range(1, max_+1)))
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        max_ = max(nums)
        lists = list(filter(self.is_prime, range(1, max_+1)))
        num = self.calc(nums) 
        number = set()
       
        # while num != 1:
      
        count = 0
        for i in lists:
            if num % i == 0:
                  
                count+=1
                num = num // i
              
        return count

            
            