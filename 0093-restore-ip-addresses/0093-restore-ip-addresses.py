class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []
        def isValid(cur):
            if int(cur) > 255 or (cur[0] == "0" and len(cur) > 1):
                     return False
            return True 

            
              
        if n > 12:
            return result
        def backtrack(index , curr):
            if index == n or len(curr) == 4:
                if index == n and len(curr) == 4:
                    result.append(".".join(curr))
            
            
            for indexj in range(index , min(index + 3 , n)):
                cur = s[index:indexj+1]
                
                if isValid(cur):
                    
                    curr.append(cur)
                    backtrack(indexj+1 , curr)
                    curr.pop()
                   
        backtrack(0 , [])
        return result 
