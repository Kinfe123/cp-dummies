class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = 0
        arr = []
        for i in range(len(nums)):
            counter = 0
            for j in nums:
                if nums[i]>j:
                    counter+=1
                    
            arr.append(counter)
                    
        return arr   
  
                    