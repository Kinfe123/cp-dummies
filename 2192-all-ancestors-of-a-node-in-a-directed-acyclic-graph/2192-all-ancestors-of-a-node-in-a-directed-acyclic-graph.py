class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        result = [set() for _ in range(n)]
        graph = defaultdict(list)
        glo_visited = set()
        indegree = [0 for _ in range(n)]
        for f , to in edges:
            indegree[to]+=1
            
            graph[f].append(to)
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            # print('the curr: ' , curr)
            #the logic goes here
            
            for nei in graph[curr]:
                # result[nei].add(curr)
            
                result[nei].update(result[curr], [curr])
                indegree[nei]-=1
                if indegree[nei] == 0:
                    # result[curr] = sorted(list(result[curr]))
                    q.append(nei)
          
        result = [sorted(list(i)) for i in result]
    
        return result
            
            