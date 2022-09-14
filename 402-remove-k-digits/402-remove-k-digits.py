class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = []
        for i in nums:
            while stack and stack[-1] > i and k > 0:
                k-=1
                stack.pop()
            stack.append(i)
        stack = stack[:len(stack) - k]
        result = "".join(stack)
        return str(int(result)) if result else "0"
        