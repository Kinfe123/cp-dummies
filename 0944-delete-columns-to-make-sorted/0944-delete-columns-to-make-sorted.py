class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        lists = []
        counter = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                lists.append(strs[j][i])
         
            st1 = "".join(lists)
            if st1 != "".join(sorted(st1)):
                
                counter+=1
            st1=""
            lists = []
        return counter