class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                letter = ""
                while stack[-1] != "[":
                    letter = stack.pop() + letter
                stack.pop()
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                stack.append(int(number) * letter)
        return "".join(stack)
        