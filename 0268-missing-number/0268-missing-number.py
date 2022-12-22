class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lists = [i for i in range(len(nums)+1) if i not in nums]
        # print(lists)
        x = lists.pop()
        return x 