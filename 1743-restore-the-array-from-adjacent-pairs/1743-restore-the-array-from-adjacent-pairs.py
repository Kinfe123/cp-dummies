class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        map_ = defaultdict(list)
        lists = []
        for each in adjacentPairs:
            u1 , u2 = each 
            map_[u1].append(u2)
            map_[u2].append(u1)
            lists.append(u1)
            lists.append(u2)
        visited = set()
        
        result = []
        def dfs(node):
            visited.add(node)
            result.append(node)
            for nei in map_[node]:
                if nei not in visited:
                    
                    
                    dfs(nei)
                    
        for keys , values in map_.items():        
            if len(values) == 1:
                dfs(keys)
    
        return result[:-1]

        
        