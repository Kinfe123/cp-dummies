class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        map_ = {i:i for i in string.ascii_lowercase}
        
        def find(x):
            
            if x != map_[x]:
                map_[x] = find(map_[x])
            return map_[x]
        def union(v1 , v2):
            r1,r2 = find(v1),find(v2)
            if r1 > r2:
                map_[r1] = r2
            else:
                map_[r2] = r1
            
        for u,v in zip(s1 , s2):
          
            union(u , v)
            
        print(map_)   
        res = []
        for i in baseStr:
            res.append(find(i))
            
        return ''.join(res)
            
        
                