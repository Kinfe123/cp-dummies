class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unbalancedO = 0
        unbalancedC = 0
        for i in s:
            if i == "(":
                unbalancedO+=1
            elif i == ")":
                if unbalancedO > 0:
                    unbalancedO -=1
                else:
                    unbalancedC +=1 
        return unbalancedC + unbalancedO
        