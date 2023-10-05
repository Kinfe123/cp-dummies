class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graphs = defaultdict(list)
        i = 0
        for u , v in edges:
            graphs[u].append((v , succProb[i]))
            graphs[v].append((u , succProb[i]))
            i+=1
        heap = [(-1 , start_node)]
        
        heapq.heapify(heap)
        visited = [0 for _ in range(n)]
        
        while heap:
            prob , node = heappop(heap)
           
            if node == end_node:
                return -1 * prob
            
            # if visited[node]:
            #     continue
            visited[node] = 1
            for nei , probs in graphs[node]:
                # print(nei , probs , ' values')
                if not visited[nei]:
                    heapq.heappush(heap , (probs * prob  , nei ))
        return 0
          
        
    