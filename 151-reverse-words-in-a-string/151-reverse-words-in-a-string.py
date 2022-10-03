class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        output = []
        for i in range(len(lst)-1 , -1 , -1):
            output.append(lst[i])
        return " ".join(output)
            
        