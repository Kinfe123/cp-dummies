class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if(n == 1):
            print(0)
            return
 
        # Allocate memory for temporary arrays left[] and right[]
        left = [0]*n
        right = [0]*n

    
        prod = [0]*n

        
        left[0] = 1

        
        right[n - 1] = 1

        # Construct the left array
        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]

        # Construct the right array
        for j in range(n-2, -1, -1):
            right[j] = nums[j + 1] * right[j + 1]

        for i in range(n):
            prod[i] = left[i] * right[i]

        
        return prod

