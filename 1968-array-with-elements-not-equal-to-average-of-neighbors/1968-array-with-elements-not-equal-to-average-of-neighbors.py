class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        new_arr = []
        
        l , r = 0 , len(nums) -1
        while len(nums) != len(new_arr):
            new_arr.append(nums[l])
            l+=1
            if l <=r:
                new_arr.append(nums[r])
                r-=1
        return new_arr
        