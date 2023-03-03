class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums)-1
        result = len(nums)
        if target<=nums[0]:
            return 0
        if(nums[len(nums)-1]<target):
            return len(nums)
        if(nums[len(nums)-1]==target):
            return len(nums)-1
        
        while left <= right:
            mid = (left + (right-left)//2)
            if nums[mid] == target:
                result = mid
                return mid
            elif nums[mid-1] <= target < nums[mid]:
                
                result = mid
                right = mid - 1
                
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
            
                left = mid+1
        return result
        