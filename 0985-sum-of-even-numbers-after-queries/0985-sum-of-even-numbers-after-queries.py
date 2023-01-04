class Solution:
    


    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
      
        summed = sum(i for i in nums if i % 2==0)
        result = []
        for values , index in queries:
     
            if nums[index] % 2 == 0:
                summed-=nums[index]
            nums[index] += values
            # WE are checking if we could get an even number after perfoming 
            #the query on the specific index if it is we need it to part of the sum on each 
            # query such that we would have appended it to the stack
            if nums[index] % 2 == 0:
                summed+=nums[index]
            result.append(summed)
        return result 