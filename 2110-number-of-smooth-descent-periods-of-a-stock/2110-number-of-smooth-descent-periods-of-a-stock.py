class Solution:
    def getDescentPeriods(self, nums: List[int]) -> int:
#         count = 1
#         start = 0
#         end = 0
#         for i in range(1 , len(nums)):
#             if nums[i] == nums[i-1] -1:
#                 count+=i-start+1
#             else:
#                 start = i 
#                 count+=i-start+1

#         return count 

        count , start , answer = 0 , 0 , 0
        previous = -math.inf
        
        for curr in nums:
            if previous - curr == 1:
                count+=1
            else:
                count = 1
                
            answer+=count 
            previous = curr
            
        return answer
    