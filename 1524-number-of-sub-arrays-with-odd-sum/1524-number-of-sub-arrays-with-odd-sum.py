class Solution:
    def numOfSubarrays(self, nums: List[int]) -> int:
        running_sum = 0
        even = 1
        odd = 0
        answer = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum % 2 == 1:
                answer += even 
                odd+=1
            else:
                answer+=odd
                even+=1
        return answer % (10**9 + 7)
            
   
            