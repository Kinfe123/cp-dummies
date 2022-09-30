class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack: 
                
                if i == stack[-1]:
                    stack.append(i)
                elif i.lower() == stack[-1] or i.upper() == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return "".join(stack)
            