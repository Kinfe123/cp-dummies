class Solution:
    def printVertically(self, s: str) -> List[str]:
        lists = s.split(" ")
        temp = []
        max_ = 0

        for i in range(len(lists)):
            max_ = max(max_  , len(lists[i]))

        for i in range(len(lists)):
            if len(lists[i]) < max_:
                lists[i] = lists[i] + (" " * (max_ - len(lists[i])))


        for i in range(max_):
            st = ""
            for j in range(len(lists)):
                st+=lists[j][i]
            temp.append(st)

        nn = []
        for i in temp:
            nn.append(i.rstrip())
        return nn
    
    
