class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       
        left_max = [0] * len(nums)
        right_max = [0] * len(nums)
        for i in range(len(nums)):
            if i % k == 0:
                left_max[i] = nums[i]
            else:

                left_max[i] = max(left_max[i-1] , nums[i])
        copy = nums.copy()
        for i in range(len(nums)-1 , -1 , -1):
            if (i+1) % k == 0:
                right_max[i] = copy[i]
            else:

                right_max[i] = nums[i] if i == len(nums)-1 else max(right_max[i+1] , copy[i])        

        sliding = []
        for i in range(len(nums)-k+1):
            result = max(right_max[i] , left_max[i-1+k])
            sliding.append(result)
        return sliding



