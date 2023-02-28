class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #since we have a constraint we should have to consider
        #2**31 can be rephrase to 4**16 approxm.
        return n in [4 ** i for i in range(16)]