class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        result = []
        cache = defaultdict(int)
        def generatePower(n):
            if n in cache:
                return cache[n]
            
            if n == 1:
                
                return 0
            elif n % 2:
                cache[n] =  1 + generatePower(n * 3 + 1)
            else:
                cache[n] = 1 + generatePower(n // 2)
            return cache[n]
            
        mapped = defaultdict(int)
        for i in range(lo, hi+1):
            mapped[i] = generatePower(i)
            
        sorted_one = list(sorted(mapped.items() , key=lambda x: x[1]))
        
        return sorted_one[k-1][0]
            