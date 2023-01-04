class Solution:
    def addSpaces(self, text: str, spaces: List[int]) -> str:
        
        
 
        spaces = [0] + spaces 
        res = []
        for i in range(1 , len(spaces)):

            res.append(text[spaces[i-1]:spaces[i]])
        res.append(text[spaces[-1]:])


        res = " ".join(res)
        return res