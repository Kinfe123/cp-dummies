class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        visited = set()
        res = False
        def dfs(index):
            nonlocal res 
            if index >= len(nums)-1:
                
                return True
            next_ = index+1
            visited.add(index)
            for node_ in range(next_ , min(len(nums) , index+nums[index] + 1)):
                if node_ not in visited and dfs(node_):
                   
                    return True 
            
        
            
                    
            
            return False
            
        return dfs(0)
            
        # return res
       