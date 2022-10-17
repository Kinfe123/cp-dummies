class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left_b , right_b = 0 , 0
        for i in range(len(s)):
            if s[i] in "(*":
                left_b += 1
            else:
                left_b -= 1
            if s[len(s)-i-1] in "*)":
                right_b +=1
            else:
                right_b-=1
            if left_b < 0 or right_b < 0:
                return False
        return True
                
#         open_bracket , closed_bracket = 0 , 0
#         #(*) 
#         #1 0 -1 = 0
#         total = 0
#         if len(list((filter(lambda x: x != "*" , list(s))))) % 2:
#             return False
#         for i in range(len(s)):
#             if s[i] == ")":
#                 open_bracket-=1
#                 closed_bracket+=1
                
#             elif s[i] == "(":
#                 closed_bracket-=1
#                 open_bracket+=1
#             elif s[i] == "*":
#                 if closed_bracket == open_bracket:
#                     total += closed_bracket+open_bracket
#                 elif (closed_bracket - open_bracket) == 1:
#                     total+=closed_bracket+open_bracket-1
#                 elif open_bracket - closed_bracket == 1:
#                      total+=closed_bracket+open_bracket+1
#         return total == 0 
                    
                    
                