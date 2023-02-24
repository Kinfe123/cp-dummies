class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_ = {N:I for I , N in enumerate(nums1)}
        output = [-1] * len(nums1)
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                popped = stack.pop()
                output[dict_[popped]] = i
            if i in dict_:
                stack.append(i)
        return output 

                
        