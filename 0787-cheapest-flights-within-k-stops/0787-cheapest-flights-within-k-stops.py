class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graphs = defaultdict(list)
        for i in range(len(flights)):
            curr = flights[i]
            graphs[curr[0]].append((curr[1] , curr[2]))
        print(graphs[src])
        
        # heap = [(0 , src)]
        min_node , min_cost = float('inf') , float('inf')
        for u , v in graphs[src]:
            if v < min_cost:
                min_cost = v
                min_node = u
        
                
            
        s = [float('inf') for _ in range(n)]
        # s[0] = 0
        cost = 0
        visited = [float('inf') for _ in range(n)]
        # moves = -1
        heap = [(-1, 0 , src)]
        heapq.heapify(heap)
        while heap:
            moves , curr_d , curr_node = heapq.heappop(heap)
            # moves+=1
            if moves > k or s[curr_node] < curr_d:
                continue
            s[curr_node] = curr_d
            for chld , w in graphs[curr_node]:
                heapq.heappush(heap, (moves + 1 , curr_d + w , chld))
                        
       
        # return s[-1]
        print(s)
        if s[dst] == float('inf'):
            return -1
       
        
        else:
            return s[dst]
    
        
            
            