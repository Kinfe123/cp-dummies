class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        diffList = [x - y for x , y in zip(nums1 , nums2)]

        result = []
        answer = 0
        for i in range(len(diffList)):
            answer+=bisect_right(result  , diffList[i])
            bisect.insort(result , diffList[i] - diff )
        return answer