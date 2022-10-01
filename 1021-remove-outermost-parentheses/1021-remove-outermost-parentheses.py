class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        opened = 0
        laststart = 0
        for i, c in enumerate(s):
            if c == "(":
                opened += 1
            else:
                opened -= 1
            if opened == 0:
                ans.append(s[laststart+1:i])
                laststart = i+1
        return "".join(ans)
        