class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_ = {"2":'abc' , "3":'def' , "4":'ghi' , "5":'jkl' , "6":'mno' , "7":'pqrs' , '8':'tuv' , "9":'wxyz'}
        sti = str(digits)
        process = []
        for i in sti:
            process.append(map_[(i)])
        take = process[:]
        process = "".join(process)
  
        result = []
        def dfs(curr , index ):
            if len(curr) == len(sti):
                result.append(curr)
                return 
            
            
            
            dealing  = map_[digits[index]]
            for i in dealing:
                # curr = curr + i
                dfs(curr + i , index+1)
                # curr.pop()
                
        if digits:
            dfs("" , 0)
        
        return result
                
        