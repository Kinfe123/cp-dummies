class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic_ = {}
        for i in range(len(s)):
            dic_[s[i]] = i
        endPoint , stretched , result = 0 , 0 , []
        for index , character in enumerate(s):
            stretched+=1
            endPoint = max(endPoint , dic_[character])
            
            if index == endPoint:
                result.append(stretched)
                stretched=0
        return result 