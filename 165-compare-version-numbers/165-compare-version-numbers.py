class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        i , j = 0 , 0
        ver1 = version1.split(".")
    
        ver2 = version2.split(".")
      
        while i < len(ver1) or j < len(ver2):
            conv1 = int(ver1[i]) if i < len(ver1) else 0
            conv2 = int(ver2[j]) if j < len(ver2) else 0
            if conv1 != conv2:
                if conv1 < conv2:
                    return -1 
                elif conv1 > conv2:
                    return 1
            if i < len(ver1):
                i+=1
            if j < len(ver2):
                j+=1
        return 0
            
        