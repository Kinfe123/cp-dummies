class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [ ['hope' , 0]]
        for i in range(len(s)):
            curr = s[i]
            if stack[-1][0] == curr:
                stack[-1][1]+=1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([curr , 1])
        st = ''
        for k , v in stack:
            st+=(k * v)
        return st
        