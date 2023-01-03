class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''' what we basically will be doing is that we will be keeping track of the 
        the min and max so that we can recompute later for finding the max of the product that we can get by multiplying the minimum number with the min to get the larger min number 
        
        
        '''
        result = max(nums)
        min_curr  , max_curr = 1 , 1
        for i in nums:
            if i == 0:
                min_curr  , max_curr = 1 , 1
                continue
            temp = max_curr * i
            #since max value might be changed on next line 
            max_curr = max(i * min_curr , i*max_curr , i)
            min_curr = min(temp  , i*min_curr , i)
            #to keep track of the current max product and min product that we have got by fat 
            #make it easier to compute the max product that we could get from the given 
            result = max(result , max_curr)
        return result