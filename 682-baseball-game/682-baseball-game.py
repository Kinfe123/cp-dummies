class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
        
            if i.lstrip('-+').isdigit():
                
                stack.append(int(i))
            elif i == "+":
                prev_1 , prev_2 = stack[-1] , stack[-2]
                stack.append(int(prev_1) + int(prev_2))
            elif i == "D":
                stack.append(int(stack[-1]) * 2)
            elif i == "C":
                stack.pop()
                
        return sum(stack)

        