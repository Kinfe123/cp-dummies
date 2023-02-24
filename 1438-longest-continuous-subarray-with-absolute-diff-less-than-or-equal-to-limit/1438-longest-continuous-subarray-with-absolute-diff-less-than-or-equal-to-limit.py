class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque([])
        min_q = deque([])
        ln = float('-inf')
        left = 0
        for i in range(len(nums)):
            while max_q and nums[i] > max_q[-1]:
                max_q.pop()
            while min_q and nums[i] < min_q[-1]:
                min_q.pop()
            
            min_q.append(nums[i])
            max_q.append(nums[i])
            
            
            if max_q[0] - min_q[0] <= limit:
                ln = max(ln , i-left+1)
                
            else:
                
                if max_q[0] == nums[left]:
                    max_q.popleft()
                if min_q[0] == nums[left]:
                    min_q.popleft()
                left+=1
        return ln
                
        