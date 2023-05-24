class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        sum_ = 0
        number = [1]*numOnes + [0]*numZeros + [-1] * numNegOnes
        for i in range(k):
            sum_+=number[i]
        return sum_