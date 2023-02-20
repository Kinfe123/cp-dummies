class Solution:
    def reverseWords(self, s: str) -> str:
        result = [i[::-1] for i in s.split()]
        return " ".join(result) 
        
        