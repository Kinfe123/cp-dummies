class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        adj = defaultdict(list)
        for i in range(len(graph)):
            adj[i] = graph[i]
        
                
       
    
        
        prev_parent = []
        
        def dfs(node , result , paths):
            
            if node == len(graph)-1:
                    
                result.append(paths.copy())
                    
                return 
          
            
            
            for i in adj[node]:
                paths.append(i)
                
                dfs(i , result ,paths)
                paths.pop()
                  
                
               
                

        
            
        
        result = []
        paths = []
        paths.append(0)
        dfs(0 , result , paths)
        
        return result
        