class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graphs = [[] for _ in range(n)]
        for u , v  , time in times:
            graphs[u-1].append((v-1 , time))
        
            
        heap = [(0 , k-1)]
        heapq.heapify(heap)
        max_ = float('-inf')
        d = [float('inf') for _ in range(n)]
        # d[0] = 0
        visited = [0 for _ in range(n)]
        while heap:
            time , node = heapq.heappop(heap)
            d[node] = min(time , d[node])
            if not visited[node]:
                visited[node]= 1
                for nei , t in graphs[node]:
                    if t + time  < d[nei]:
                        heapq.heappush(heap , (t+time , nei))
                
        print(d)
        ans = max(d)
        if ans == float('inf'):
            return -1
        else:
            return ans
            

        