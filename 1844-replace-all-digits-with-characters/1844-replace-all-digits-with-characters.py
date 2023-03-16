class Solution:
    def replaceDigits(self, s: str) -> str:
        lists = list(s)
        for i in range(1 , len(s) , 2):
            diff =  ord(lists[i-1]) - ord('a')
            summed = (int(lists[i]) + diff) % 26
            summed+=97
            lists[i] = chr(summed)
        return "".join(lists)
            
            
        