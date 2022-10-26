class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left , right = 0 , k
        counter = 0
        answer = 0
        vowels = ["a" , "e" , "i" , "o" , "u"]
        for i , v in enumerate(s):
            if i>=k:
                if s[i-k] in vowels:
                    counter-=1
            if s[i] in vowels:
                counter+=1
            answer = max(answer ,  counter)
        return answer
            

            
            
        