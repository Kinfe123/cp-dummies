class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        
        a,b = Counter(word1),Counter(word2) 
        c,d = a.copy(),b.copy()
        for i in a: 
            for j in b: 
                c[i], c[j], d[j], d[i] = c[i]-1, c[j]+1, d[j]-1, d[i]+1
                if not c[i]: del c[i] 
                if not d[j]: del d[j] 
                if len(c)==len(d): return True #after swap 
                c,d = a.copy(),b.copy() 
        return False
#         setA = set()
#         setB = set()
#         map_1 = Counter(word1)
#         map_2 = Counter(word2)
#         for keys , values in map_1.items():
#             setA.add(keys)
#         for keys , values in map_2.items():
#             setB.add(keys)
#         l_1 = len(setA)
#         l_2 = len(setB)
        
   
#         # if l_1 == l_2:
#         #     return True
#         if abs(l_1 - l_2) == 1:
#             for i in setA:
#                 if i not in setB:
#                     if map_1[i] > 1:
#                         key1 = list(map_1.keys())[0]
#                         map_1[key1]-=1
#                         if map_1[key1] == 0:
#                             del map_1[key1]
#                         if len(map_1) == len(map_2):
#                             return True  
#                         # return True 
                
                    
                    
#         return False
       