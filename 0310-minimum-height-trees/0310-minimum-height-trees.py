class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indeg = [0] * n
        if n <= 2:
            return [x for x in range(n)]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[u]+=1
            indeg[v]+=1
        
        min_ = float('inf')
        q = deque()
        for i in range(n):
            if len(adj[i])==1:
                q.append(i)
                
        
        
        while n>2:
            count = len(q)
            n-=count
            for i in range(count):
                leaf = q.popleft()
                par = adj[leaf].pop()
                adj[par].remove(leaf)
                
                if len(adj[par]) == 1:
                    q.append(par)
        return list(q)
                    