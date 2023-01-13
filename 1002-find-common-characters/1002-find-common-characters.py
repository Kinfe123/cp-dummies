class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        values = [i for i in words[0]]
        result= []
        for i in range(1  , len(words)):
            for j in words[i]:
                if j in values:
                    result.append(j)
                    values.remove(j
                                 )
            values = result
            result = []
            
        return values
       
            
        