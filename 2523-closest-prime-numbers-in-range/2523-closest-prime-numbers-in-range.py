class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
       
        def SieveOfEratosthenes(num):
           
            prime = [True for i in range(num)]
        
            prime[0] = prime[1] = False  
        # boolean array


            p = 2
            sqr = math.ceil(math.sqrt(num))
            for p in range(2 , sqr):

                if (prime[p] == True):
                    
                    for i in range(p*p, num, p):
                        prime[i] = False

            return prime
        
        answer = SieveOfEratosthenes(right+1)
   
       
   
        min_ = float('inf')
        prev = 0
        result = [-1 , -1]
 
        if len(answer) < 2:
            return [-1 , -1]
        for i in range(left , right+1):
            if answer[i]:
             
                if abs(i-prev) < min_:
                    
                    min_ = min(min_ , i-prev)
              
                    result[0] = i - min_
                    result[1] = i
                prev = i
        if result[0] == 0:
            return [-1 , -1]
                
        return result
                
                
                
            
            
            
            