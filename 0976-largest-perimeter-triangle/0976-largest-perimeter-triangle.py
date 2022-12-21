class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #to reduce the time comp we can start looking for the right most element 
        #since we are asked for the largest perimeter of triangle, we should 
        #be good if the right most element doesnot work , it also doesnt work for the 
        #rest of the lefty elements
        #time - O(nlogn) - since we use sorting 
        #space - O(1) - since sort function sort in place at best case
        nums.sort()
        for i in range(len(nums)-1 , 1,  -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                return nums[i] + nums[i-2] + nums[i-1]
        return 0
                
        