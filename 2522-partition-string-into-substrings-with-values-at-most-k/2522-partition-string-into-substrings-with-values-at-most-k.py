class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        counter = 1
        cmp_alp = 0
        for char in s:
            cmp_alp = cmp_alp * 10 + int(char)
            
            
            if cmp_alp > k:
                cmp_alp = int(char)
                counter+=1
            if cmp_alp > k:
                return -1 
        return counter
            
            
        
        
        