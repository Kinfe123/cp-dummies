class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            search_ = 0
            for j in range(len(nums)):
                if (nums[j] >> i) & 1:
                    search_+=1
            search_ = search_ % 3
            #since we need to consider those that is duplicated
            if search_ != 0:
                result+=2**i
            
        val = 2**31
        if result >= val:
            result-=val*2
        return result
                
                
        