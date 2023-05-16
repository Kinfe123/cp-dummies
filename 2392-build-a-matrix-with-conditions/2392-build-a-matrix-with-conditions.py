class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def generateOrder(conditions):
            map_ = defaultdict(list)
            indeg = [0] * k
            for u , v in conditions:
                map_[u].append(v)
                indeg[v-1]+=1
            
            q = deque([])
          
            for i in range(k):
                if indeg[i]==0:
                    q.append(i+1)
    
            order = []
            while q:
                curr = q.popleft()
                order.append(curr)
                for child in map_[curr]:
                    indeg[child - 1] -= 1
                    if not indeg[child-1]:
                        q.append(child )
            return order
        row_relations = generateOrder(rowConditions)

        col_relations = generateOrder(colConditions)
        R = len(row_relations)
        C = len(col_relations)
        if R  < k or C < k:
            return []
        result = [[0] * k for _ in range(k)]
        for r in range(len(row_relations)):
            row , col = r  , col_relations.index(row_relations[r])
            result[row][col] = row_relations[r]
        return result 
                    
                