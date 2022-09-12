class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left , right = 0 , len(nums)-1
        lists = []
        for i in range(len(nums)//2):
            lists.append([nums[left] , nums[right]])
            left+=1
            right-=1

        listed = [sum(i) for i in lists]
        return max(listed)