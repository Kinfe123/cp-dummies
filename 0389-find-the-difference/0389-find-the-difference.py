class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_total = sum([ord(i) for i in s ])
        t_total = sum([ord(i) for i in t])
        return chr(t_total-s_total)
        
        