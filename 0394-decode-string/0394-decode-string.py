class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                curr_string = ''
                while stack[-1] != '[':
                    curr_string = stack.pop() + curr_string
                #remove [
                
                stack.pop()
                # k = 0
                p = 0
                summed = 0
                while stack and stack[-1].isdigit():
                    curr = stack.pop()
                    summed += (10**p) * int(curr)
                    p+=1
                stack.append(curr_string * summed)
        return "".join(stack)
                    
        