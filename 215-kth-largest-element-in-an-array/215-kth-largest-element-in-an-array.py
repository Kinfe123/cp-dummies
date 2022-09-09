class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        value = 0
        for i in range(k):
            value = heapq.heappop(nums)
        if value > 0:
            return -value 
        else:
            return abs(value)
            
        