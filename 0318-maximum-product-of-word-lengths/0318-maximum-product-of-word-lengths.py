class Solution:
    def maxProduct(self, words: List[str]) -> int:
        #bruteforce approach 
        on_mask = [0] * len(words)
        max_ = 0
        lens = [0] * len(words)
        for i in range(len(words)):
            for each in words[i]:
                on_mask[i]|=1 << (ord(each) - 97)
            lens[i] = len(words[i])
        #The idea is that we will be setting on the bit for marking the existense of the specific char
        #which will helps up to detect for the future and compute their AND which will tell us whether the given 
        #character is unique unique in refernce to its pair
        for i in range(len(words)):
            for j in range(i+1 , len(words)):
                if not (on_mask[i] & on_mask[j]):
                    max_ = max(max_ , lens[i] * lens[j])
        return max_
                
                
                  
                 
       
        