class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        string1 = list(s1)
        string2 = list(s2)
        map_for_swap = {}
        lists = []
        
        if string1 == string2:
            
            return True 
        else:
            for i in range(len(string1)):
                if string1[i] != string2[i]:
                        map_for_swap[i] = string2[i]
                        lists.append(string2[i]) 
        # string1 = "".join(string1)
        # string2 = "".join(string2)
        list1 = list(map_for_swap.keys())
        if len(list1) < 2:
            return False
        index_of_1  = list1[0]
        index_of_2 = list1[1]
        string2[index_of_1] , string2[index_of_2] = string2[index_of_2] , string2[index_of_1]
        
       
        
        
        return True if string1 == string2  else False
             
          
                    
        