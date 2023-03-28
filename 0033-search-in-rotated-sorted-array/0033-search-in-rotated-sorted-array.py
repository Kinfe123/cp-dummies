class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low , high = 0 , len(nums)-1
        if target not in set(nums):
            return -1
        
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[high]:
                if target >= nums[low] and target <= nums[mid]:
                    high = mid
                else:
                    low = mid+1
            
            else:
               if target >=  nums[mid] and target <= nums[high]:
                    low = mid+1
               else:
                    high = mid
                
         
        return high
        