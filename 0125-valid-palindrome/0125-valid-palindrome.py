class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        converted = ''.join([i.lower() for i in s if i.isalnum() ])
        l  , r = 0 ,  len(converted)-1
        # print(converted)
        isTrue = False
        while l < r:
            isTrue = converted[l] == converted[r]
            l+=1
            r-=1
            if isTrue == False:
                
                return False
                # break
                
        return True
                
            
            
            
        