class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        slow = 0
        fast = 1
        while fast < n:
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow] = nums[fast]
            fast+=1
        return slow+1

        