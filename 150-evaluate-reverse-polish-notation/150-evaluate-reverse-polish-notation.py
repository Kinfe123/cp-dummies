class Solution:
    def evalRPN(self, token: List[str]) -> int:
        stack = []
        for i in range(len(token)):

            if token[i] in "+-/*":
                if token[i] == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token[i] == "-":
                    a , b = stack.pop() , stack.pop()
                    
                    stack.append(b - a)
                elif token[i] == "*":
                    stack.append(stack.pop() * stack.pop())
                elif token[i] == "/":
                    a , b = stack.pop() , stack.pop()
                    
                    stack.append(int(b / a))
            else:
                stack.append(int(token[i]))
                    
        return stack[0]
            