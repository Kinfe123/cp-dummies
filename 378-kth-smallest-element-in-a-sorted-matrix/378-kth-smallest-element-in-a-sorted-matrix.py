class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        new_arr = []
        for i in matrix:
            for j in i:
                new_arr.append(j)
        heapq.heapify(new_arr)
        value = 0
        for i in range(k):
            value = heapq.heappop(new_arr)
        return value 
            
                
                