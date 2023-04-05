class Solution:
    def minSteps(self, n: int) -> int:
        primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        if n == 1:
            return 0
        res = 0
        # the idea is that every number can be expressed as a prime factor such that the cost operation will be 
        # the sum of those prime factors like 27 = 3 ** 2 will have 3 + 3 = 6
        while n > 1:
            for i in range(2 , n+1):
                while n % i == 0:
                    res += i
                    n //= i
        return res