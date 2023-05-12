class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        result = []
        graph = defaultdict(list)
        glo_visited = set()
        for f , to in edges:
            graph[to].append(f)
    
            
        def dfs(node , res):
            visited.add(node)
            
            
            for each in graph[node]:
               
                if each not in visited:
                    
                    dfs(each , res)
            
     
            #down the path we should not have to get in to our parents
            
            # res.sort()
            # if res not in result:
            #     result.append(res)
            # return 
            
        for i in range(n):
            if not len(graph[i]):
                result.append([])
            else:
                visited = set()
                
                dfs(i , [])
                #since i should have to take all of it ansestor, we have to remove the current one 
                visited.remove(i)
                result.append(sorted(set(visited)))
                
        return result
                    
        