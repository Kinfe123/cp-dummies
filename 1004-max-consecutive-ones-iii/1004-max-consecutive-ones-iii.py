class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #O(n) - time complexity
    
        l = 0
        countZero = 0
        max_ = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                countZero+=1
            while countZero > k:
                
                if nums[l] == 0:
                    countZero-=1
                l+=1
            max_ = max(max_ , r-l+1)
                
                
                    
                    
               
        return max_
                
        