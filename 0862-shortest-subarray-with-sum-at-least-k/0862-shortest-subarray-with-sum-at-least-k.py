class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque()
        summation = 0

        min_ = float('inf')
        for i in range(len(nums)):
            summation+=nums[i]
            if summation >= k:
                min_ = min(min_ , i+1)
            
            currIdx = float('-inf')
            currSum = float('-inf')
            
            while len(q) and summation - q[0][0] >= k:
                currSum , currIdx = q.popleft()
              
                
                
            if currSum != float('-inf'):
                min_ = min(min_ , i-currIdx)
              
            while len(q) and q[-1][0] >= summation:
                q.pop()
            q.append([summation , i])
        return min_ if min_ != float('inf') else -1
            