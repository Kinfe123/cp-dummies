class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # parent = list(range(len(stones)))
        max_row = 0
        max_col = 0
        
        for u , v in stones:
            max_row = max(max_row , u)
            max_col = max(max_col , v)
        parent = list(range(max_col + max_row + 2))
        rank = [1 for i in range(max_col + max_row + 2)]
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        def union(v1 , v2):
            r1 , r2 = find(v1), find(v2)
            if rank[r1]  > rank[r2]:
                parent[r2] = r1
                rank[r1]+=rank[r2]
            elif rank[r2] > rank[r1]:
                parent[r1] = r2  
                rank[r2]+=rank[r1]
            else:
                parent[r1] = r2
                rank[r2]+=1
        set_ = set()
        
        for u , v in stones:
            node_r = u 
            node_c = v + max_row + 1
            union(node_r , node_c)
            set_.add(node_r)
            set_.add(node_c)
        comp_ = 0   
        for each in set_:
            # the formula will be truncate like the number of total number of stones - number of unique parent(component)
            # since we can not remove it self tho , we could remove all except itself - means there wont be no one would could help 
            # removing
            if find(each) == each:
                comp_+=1
            
        return len(stones) - comp_
            
            
        
        
            
        