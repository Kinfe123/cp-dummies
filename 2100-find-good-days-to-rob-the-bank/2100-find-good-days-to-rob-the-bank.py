
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        nonInc = [0]
        
        nonDec = [0] 
  
        current = 0
        for i in range(1 , len(security)):
            
            if security[i] <= security[i-1]:
                current+=1
                
            else:
                current = 0
            nonInc.append(current)
        current = 0
        for i in range(len(security)-2 , -1 , -1):
            if security[i] <= security[i+1]:
                current+=1
            else:
                current = 0
                
            nonDec.append(current)
        
        
        nonDec.reverse()
        
        return [i for i in range(len(security)) if nonInc[i] >= time and nonDec[i] >= time]
    
    
 