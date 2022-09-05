class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def isArth(nums):
            
            if len(nums) < 2:
                return False
            elif len(nums) == 2:
                return True 
            elif len(nums)  > 2:
                dif = nums[1] - nums[0]
                for i in range(1 , len(nums)-1):
                    if nums[i+1] - nums[i] != dif:
                        return False
                return True
        n = len(l)
        output = []
        for i in range(n):
            subarray = nums[l[i] : r[i]+1]
            subarray.sort()
            if isArth(subarray):
                output.append(True)
            else:
                output.append(False)
                
        return output
       