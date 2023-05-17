# class Solution:
#     def longestCycle(self, edges: List[int]) -> int:
#         max_ = float('-inf')
#         map_ = defaultdict(list)
        
#         for idx , val in enumerate(edges):
#             if val == -1:
#                 map_[idx].append([])
#             else:
#                 map_[idx].append(val)
  
#         def cycleDetect(node , visited , recurTrace , time):
#             visited[node] = True 
#             nonlocal max_
           
#             recurTrace[node]  = True 
#             time+=1
#             for child in map_[node]:
#                 if child and  not visited[child]:
#                     if cycleDetect(child , visited , recurTrace, time):
#                         print('I found a cycle')
#                         max_ = max(max_ , time)
#                         return True 
#                 elif child and recurTrace[child]:
#                     return True 
                
            
#             recurTrace[node] = False
            
#             return False
                
   
                
#         visited = [False]*len(edges)    
#         recurTrace = [False] * len(edges)
#         for i in range(len(edges)):
#             time = 1
#             if not visited[i] and edges[i]!=-1:
#                 if cycleDetect(i , visited , recurTrace , time):
#                     pass
                    
                
                    
#                 else:
#                     pass
                    
                    
            
            
                
#         return [max_ - 1 , -1][max_ == float('-inf')]
    
    
            
        


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        max_ = float('-inf')
        def dfs(node , map_):
            nonlocal max_
            
            visited.add(node)
            only_nei = edges[node]
            
            if only_nei not in visited and only_nei != -1:
                map_[only_nei] = map_[node] + 1
                dfs(only_nei , map_)
            elif only_nei in map_:
                max_ = max(max_ , map_[node] - map_[only_nei] + 1)
                
        for node in range(len(edges)):
            if node not in visited:
                map_ = defaultdict(int)
                map_[node] = 1
                dfs(node , map_ )
        return [max_ , -1][max_ == float('-inf')]
                
                
            
        