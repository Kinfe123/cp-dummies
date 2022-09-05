class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        counter = 0
        arr = []
        for i in range(len(nums)):
            counter = 0
            for j in nums:
                if nums[i]>j:
                    counter+=1
                    
            arr.append(counter)
                    
        return arr   
    
solution = Solution()
nums = [8,1,2,2,3]
print(solution.smallerNumbersThanCurrent(nums))

            
        