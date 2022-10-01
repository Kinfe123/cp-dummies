
class Solution:
    def findUnsortedSubarray(self, A):
        ans, count = 0, 0
        for a, b in zip(A, sorted(A)):
            if a != b or count:
                count += 1
                if a != b: ans = count
        return ans