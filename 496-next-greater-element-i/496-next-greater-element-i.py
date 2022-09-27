class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsMap = {n:i for i , n in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            current_value = nums2[i]
            while stack and stack[-1] < current_value:
                popped = stack.pop()
                index = numsMap[popped]
                result[index] = current_value 
            if current_value in numsMap:
                stack.append(current_value)
        return result 
                
        