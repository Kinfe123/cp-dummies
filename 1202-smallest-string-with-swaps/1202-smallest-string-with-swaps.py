class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        map_ = {i:i for i in string.ascii_lowercase}
        parent = [i for i in range(len(s))]
        rank = [1 for _ in range(len(s))]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
            return temp
        def union(v1, v2):
            r1 , r2 = find(v1) , find(v2)
            if r1 != r2:
                if rank[r1] > rank[r2]:
                    parent[r2] = r1
                    rank[r1] += rank[r1]
                elif rank[r1] < rank[r2]:
                    parent[r1] = r2
                    rank[r2]+=rank[r1]
                else:   
                    parent[r1] = r2
                    rank[r2] += 1
            
            
        
            
                
             
        
        res = []
        for u , v in pairs:
            union(u , v)
            
        dict_ = defaultdict(list)
        for i in range(len(s)):
            dict_[find(i)].append(s[i])
        
        for keys , values in dict_.items():
            values.sort(reverse=True)
        for i in range(len(s)):
            val = find(i)
            res.append(dict_[val].pop())
        return ''.join(res)
        
                