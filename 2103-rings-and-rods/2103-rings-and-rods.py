from collections import defaultdict

class Solution:
    def countPoints(self, rings: str) -> int:
        lists = []
        i = 0
        while i <= len(rings)-1:
            lists.append(rings[i:i+2])
            i+=2
        
        counter = 0
        map_2 = defaultdict(list)
     
      
        for i in range(len(lists)):
            
            color = lists[i][0]
            rod_position = lists[i][1]
            map_2[rod_position].append(color)
            
                        
            
        rgb = ['R' , 'G' , 'B']  
        for keys , values in map_2.items():
            if set(values) == set(rgb):
                counter+=1
                
        
        return counter 
            
            