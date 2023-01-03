class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        '''max_ = float('-inf')
        l = 0 
        pro = 1
        k = 3
        for r in range(len(nums)):
            pro*=nums[r]
            while r - l+1 > k:
                pro/=nums[l]
                pro = int(pro)
                l+=1
            if r-l+1==k:
                max_ = max(max_ , pro)
                
        return max_
        
        if it were conti. subarray 
        
        
        for the lsy of the number to be calculated [1 , 2 , 3 , 4]
        '''
        
        nums.sort()
        lenght = len(nums)
        #To consider the negative and posiitve one which yeilds max product
        #To get the 2 -ve and multiplied it with the 1 largest positive that are found 
        #in our lists [-2 , -1 , 2, 6] =  6 * -2 * -1
        return max(nums[0] * nums[1] * nums[lenght-1]  , nums[lenght-2] * nums[lenght-1] * nums[lenght-3])
        
            
        
        
                
            
        
        