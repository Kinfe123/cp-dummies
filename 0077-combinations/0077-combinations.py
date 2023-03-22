class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        current = []
        lists = [i for i in range(1 , n+1)]
        visited = set()
        
        def backtrack(index):
        
            if len(current) == k:
                result.append(current[:])
                return 
            
            
            for i in range(index,n+1):
                current.append(i)
                backtrack(i+1)
                current.pop()
            
                
                
                
           
        
        backtrack(1)
        return result
            