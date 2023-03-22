class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result , current = []  , []
        def backtrack(index):
            if len(current) == len(nums): 
                result.append(current[:])
                return 
            for i in range(len(nums)):
                current.append(nums[i])
                backtrack(i+1)
                current.pop()
                
        backtrack(0)
        
        post = []
        visited = set()
        for i in result:
            
            
            if len(set(i)) == len(nums):
                post.append(i)
           
                
        return post
        # return result 
        