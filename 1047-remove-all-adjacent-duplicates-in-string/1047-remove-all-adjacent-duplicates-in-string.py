class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk=[-1]
        l=[]
        for i in s:
            if stk[-1]==i:
                stk.pop()
            else:
                stk.append(i)
        stk.pop(0)
        return "".join(stk)