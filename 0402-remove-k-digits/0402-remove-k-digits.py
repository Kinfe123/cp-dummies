
class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = []
        for i in nums:
           
            while k>0 and stack and stack[-1]>i:
                k-=1
                stack.pop()
            stack.append(i)

        #handling increasing element such as 1234 we want to have the 12 
        stack = stack[:len(stack)-k]
        
            
        result = "".join(stack)
        return str(int(result)) if result else "0"
        