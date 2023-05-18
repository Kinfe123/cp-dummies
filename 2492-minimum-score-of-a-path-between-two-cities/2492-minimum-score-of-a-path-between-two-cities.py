class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        rank = [1 for _ in range(n+1)]
        min_ = float('inf')
        
        def find(x):
            temp = parent[x]
            while temp != parent[temp]:
                temp = parent[temp]
            return temp
        def union(v1 , v2 , d):
            nonlocal min_
            
            r1 , r2 = find(v1),find(v2)
            if rank[r1] > rank[r2]:
                parent[r2] = r1
                rank[r2] = rank[r1] 
                
            elif rank[r2] > rank[r1]:
                parent[r1] = r2
                rank[r1] = rank[r2]
            
            
            else:
                parent[r2] = r1
                rank[r1] += 1
         
                
            
            
        for u , v , d in roads:
            union(u , v , d)
        for i in roads:
            from_1 = find(1)
            from_x = find(i[0])
            from_y = find(i[1])
            if from_1 == from_x == from_y:
                min_ = min(min_ , i[2])
        return min_
            
            