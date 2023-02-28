class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        cur_index = 0
        nums = [i for i in range(1, n+1)]
        while len(nums) > 1:
            to_remove =( cur_index + k - 1 )% len(nums)
            nums.remove(nums[to_remove])
            cur_index = to_remove % len(nums)
        
        return nums[0]
            
    
        