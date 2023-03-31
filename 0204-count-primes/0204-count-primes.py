class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 1 or n == 0:
            return 0
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
        
        s = SieveOfEratosthenes(n)
        
        count = 0
        for i in s:
            if i:
                count+=1
            
        return count
