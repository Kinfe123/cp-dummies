class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = low+ (high-low)//2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid-1]:
                high = mid
            else:
                low = mid+1
                
                
            
        
        