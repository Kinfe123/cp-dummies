
class Solution:
    def countVowels(self, word: str) -> int:
        comb = 0
        counter = 0
        vowels = {'a' , 'e' , 'i' , 'o' , 'u'}
        
                
        for i in range(len(word)):
            if word[i] in vowels:
                #to make sure that we have already formed the subs for those who has contained 
                #before - we have seen so far * the one that we caught
           
                comb += (i+1) * (len(word)-i)
            
        
                
        
        return comb
            
        