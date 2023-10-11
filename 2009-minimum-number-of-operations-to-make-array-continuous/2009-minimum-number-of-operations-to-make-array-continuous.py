class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sorted_num = sorted(set(nums))
        diff = sorted_num[-1] - sorted_num[0]
        if diff == len(nums)-1 and len(set(nums)) == len(nums):
        
            return 0
        else:
            min_ = float('inf')
            
            # print(sorted_num)
            for i in range(len(sorted_num)):
                t = sorted_num[i] + len(nums) - 1
               
                insert = bisect_right(sorted_num , t)
                
                min_ = min(min_ , len(nums) - insert + i)
                    
            return min_
            