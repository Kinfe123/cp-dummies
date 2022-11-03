
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        inc = [0]
        dec = [0]
        current = 0
        for i in range(1 , len(security)):
            
            if security[i] <= security[i-1]:
                current+=1
                
            else:
                current = 0
            inc.append(current)
        current = 0
        for i in range(len(security)-2 , -1 , -1):
            if security[i] <= security[i+1]:
                current+=1
            else:
                current = 0
                
            dec.append(current)
        
        
        dec.reverse()
        
        return [i for i in range(len(security)) if inc[i] >= time and dec[i] >= time]
    
    
 
        
        