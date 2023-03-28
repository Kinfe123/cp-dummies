class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_ = sorted(nums1 + nums2)
        if len(sorted_) % 2:
            return sorted_[len(sorted_)//2]
        else:
            mid = len(sorted_)//2
            return (sorted_[mid] + sorted_[mid-1])/2
        
    
        