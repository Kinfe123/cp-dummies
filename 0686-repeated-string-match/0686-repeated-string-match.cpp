class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        times = -(-len(B) // len(A)) # Equal to ceil(len(b) / len(a))
        for i in range(2):
            if B in (A * (times + i)):
                return times + i
        return -1
