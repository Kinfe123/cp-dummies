class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        #Find the peak 
        #The first and last element can not be the peak 
        max_ = 0
        for i in range(1 , len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l = r = i
                while l > 0 and arr[l] > arr[l-1]:
                    l-=1
                while r < len(arr)-1 and arr[r] > arr[r+1]:
                    r+=1
                max_ = max(max_ , (r-l+1))
        return max_
                    