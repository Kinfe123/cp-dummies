class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        setElement = set()
        current , result = [] , []
        def dfs(index):
            if index >= len(nums):
                sorted_one = sorted(current.copy())
                if tuple(sorted_one) not in setElement: 
                    result.append(tuple(current.copy()))
                    setElement.add(tuple(sorted_one))
                return 
            
            #including the element on the decision tree
            current.append(nums[index])
            dfs(index + 1)
            
            #not including the element but we will do both the including and not 
            #including on it
            current.pop()
            dfs(index + 1)
        dfs(0)
        return result
    
        