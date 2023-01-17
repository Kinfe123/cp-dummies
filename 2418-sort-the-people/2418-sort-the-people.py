class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic_ = {}
        for i in range(len(names)):
            dic_[heights[i]] = names[i]
            
        dic_ = dict(sorted(dic_.items() , reverse=True))
        result = list(dic_.values())
        return result
        
        
        
    
        