class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        result , current = [] , []
        map_ = defaultdict(int)
        max_ = 0
            
        def dfs(index):
            nonlocal max_
            
            if index >= len(nums):
                
                result.append(current.copy())
                if current.copy():
                    val = reduce(lambda x , y : x|y , current.copy())
                    max_ =  max(max_ , val)
                    # map_[tuple(current.copy())] =  val

                return 
            current.append(nums[index])
            dfs(index + 1)
            current.pop()
            
            #for not being included 
            dfs(index + 1)
        dfs(0)
        count = 0
        
        for i in result:
            if i:
                if reduce(lambda x , y : x | y , i) == max_:
                    count+=1
                
        return count
        
        