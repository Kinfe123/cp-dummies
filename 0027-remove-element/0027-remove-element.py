class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        element_tobe = []
        for i in range(len(nums)):
            if nums[i] == val:
              
                element_tobe.append(nums[i])
        for i in element_tobe:
            nums.remove(i)
            


    
        return len(nums)
        