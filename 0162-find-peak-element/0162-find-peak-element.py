class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)-1
        if len(arr) == 1:
            return 0
        if len(arr) == 2:
            if arr[0] < arr[1]:
                return 1
            else:
                return 0
        
        while low <= high:
            mid = low+ (high-low)//2
            if mid >= len(arr)-1:
                return mid
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid-1]:
                high = mid
            elif arr[mid] < arr[mid+1]:
                low = mid+1
            else:
                return mid
                
                
            
        