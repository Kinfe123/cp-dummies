class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        element_less = []
        element_greater = []
        equal_to = nums.count(pivot)

        for i in range(len(nums)):
            if pivot < nums[i]:
                element_greater.append(nums[i])
            elif pivot > nums[i]:
                element_less.append(nums[i])

        return element_less + [pivot] * equal_to + element_greater


        