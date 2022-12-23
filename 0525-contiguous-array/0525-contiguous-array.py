class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        final_answer = 0
        curr_answer = 0
        running_sum = 0
        map_ = {0:-1} # zero gain at nowhere inside the nums
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        for i in range(len(nums)):
            running_sum+=nums[i]
            if running_sum == 0:
                curr_answer = i - map_[0]
                final_answer = max(final_answer , curr_answer)
            if running_sum not in map_:
                map_[running_sum] = i
            else:
                curr_answer = i - map_[running_sum]
                final_answer = max(final_answer , curr_answer)
                '''
                If we had something like this
                
                list - [1 , 1 , 1 , 0 , 0  , 1 , 1 ]
                        1   1   1  -1   -1   1    1
                        
                after changing the 0's to -1's we can easily keep track of the 
                sum which is what we want it to be zero for equal number of 0's and 1's 
                
                lets go through the above list 
                 sum = 1  2  3  2  1   2   3
                   this is the prefix sum that we could get from the list: the thing that we could not find zero doesnt 
                   mean that we dont have the subarray that have equal no- of 0's and 1's
                 Although we could see some patterns that 1 being appearing at the 0 index and then at 4 index .. this  
                 is telling us that starting from the 0 index (not including since it is a transformation)
                 to 4 index we have the subarray that have equal number of 0's and 1's since sum doesnt change - return
                 back to where it was for such cases we keep track where it occurs using map
                
                
                '''
                
                
                
        return final_answer
                
                
                
            

                 
        
            
        