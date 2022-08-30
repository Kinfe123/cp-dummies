class Solution(object):
    def findMiddleIndex(self, nums):
        nums.append(0)
        for i in range(1,len(nums)):

            lef = (sum(nums[0:i-1]))
            rig = (sum(nums[i:]))
            if (lef == rig) : return i-1
        return -1
        