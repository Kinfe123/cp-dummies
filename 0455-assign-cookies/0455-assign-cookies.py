class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ptr_g , ptr_s = 0 ,0
        g.sort()
        s.sort()
        counter = 0
        max_ = min(g)
        size = sum(s)
        while ptr_g < len(g) and ptr_s < len(s):
            if g[ptr_g] <= s[ptr_s]:
                ptr_g+=1
                ptr_s+=1
            else:
                ptr_s+=1
        return ptr_g
                
            
        return counter
                
        
            
                
        