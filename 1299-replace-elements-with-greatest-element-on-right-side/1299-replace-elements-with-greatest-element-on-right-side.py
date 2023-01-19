class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = 0
        max_ = -1
        for i in range(len(arr)-1 , -1 , -1):
            curr = arr[i]
            arr[i] = max_
            max_ = max(curr , max_)
        return arr
            