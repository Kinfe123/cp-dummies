class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return bisect.bisect_left(arr[:arr.index(max(arr))] , max(arr))
        