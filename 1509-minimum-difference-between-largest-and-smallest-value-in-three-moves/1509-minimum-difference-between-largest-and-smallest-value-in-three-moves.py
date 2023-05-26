class Solution:
    def minDifference(self, nums: List[int]) -> int:
        lenght = len(nums)
        nums.sort()
        if lenght <= 4:
            return 0
        
        return min(b - a for a, b in zip(nums[:4], nums[-4:]))
#         first_max , first_min , second_max ,second_min = float('-inf'), float('inf') , float('-inf'), float('inf')
#         for i in range(3 , len(nums)):
        
#             first_max = max(first_max , nums[i])
#             first_min = min(first_min , nums[i])
      
#         for i in range(0 , len(nums)-3):
#             if second_max < nums[i]:
#                 second_max = nums[i]
#             # second_max_ = max(second_max , nums[i])
#             second_min = min(second_min , nums[i])
        
       
        
#         return min(first_max - first_min , second_max-second_min)
        
#         elif lenght > 4 and lenght <= 6:
#             min_ = float('inf')
#             for i in range(1 , len(nums)):
#                 min_ = min(min_ , nums[i] - nums[i-1])
#             return min_
#         else: 
            
#             smallest_three , middle_ , largest_three = nums[:3] , nums[3:len(nums)-3], nums[len(nums)-3:]
            
#             return min(middle_[0] - smallest_three[-1], largest_three[0] - middle_[-1])