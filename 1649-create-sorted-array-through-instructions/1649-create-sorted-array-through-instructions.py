class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        cost = 0
        mod = 10**9 + 7
        lists = []
        for i in range(len(instructions)):
            cost_b = bisect_left(lists , instructions[i])
            cost_a = len(lists) - bisect_right(lists , instructions[i])
          
            cost += min(cost_b , cost_a)
            bisect.insort(lists , instructions[i])
        return cost % mod
        