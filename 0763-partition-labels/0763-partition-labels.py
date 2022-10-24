class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i
            if dic[s[i]] == s[i]:
                dic[s[i]] = i
        end , res , size = 0 , [] , 0
        
        for index , char in enumerate(s):
            size+=1
            end = max(end , dic[char])
            if index == end:
                res.append(size)
                size = 0
                
        return res
            
            
            