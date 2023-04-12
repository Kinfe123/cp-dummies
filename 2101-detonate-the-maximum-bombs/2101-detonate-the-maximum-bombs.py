class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                if math.sqrt((bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1])**2)  <= bombs[i][2]:
                    graph[i].append(j)
                    # the i can detonate the j bomb
        
  
        visited = set()
        print(graph)
        def dfsify(node):
            # count = 0
            for i in graph[node]:
                if i not in visited:
                    # count +=1 
                    visited.add(i)
                    dfsify(i)
                
                    
            return len(visited)
        max_ = 0       
        for i in list(graph.keys()):
            visited.add(i)
            max_ = max(max_ , dfsify(i))
            visited = set()
            
        return max_ if max_ != 0 else 1 # because we can detonate either of the bombs

            
            