class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        pointer1 , pointer2 , answer = 0 , 0 , 0
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] <= nums2[pointer2]:
                answer = max(answer , pointer2 - pointer1)
                pointer2+=1
            else:
                pointer1+=1
        return answer
                
        