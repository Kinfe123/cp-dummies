class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #locked - 
        
        if len(s) % 2 : #Means if it odd lenghted . it can not be balanced
            
            return False
        allowed_to_change , opened_bracket, closed_bracket = 0 , 0 , 0
        for i in range(len(s)):
            if locked[i] == '0':
                opened_bracket+=1
            #When we cant make change 
            else:
                if s[i] == ')':
                    closed_bracket+=1
                    #Closed fixed bracket
                elif s[i] == '(':
                    opened_bracket+=1
                    #Opend fixed bracket
            #I have possiblity for making some opened bracker with 0
            opened_bracket+=allowed_to_change
            if opened_bracket < closed_bracket:
                #If the fixed closed bracket exceed we can not make a change 
                return False
        allowed_to_change , opened_bracket, closed_bracket = 0 , 0 , 0
        for i in range(len(s)-1 , -1 , -1):
            if locked[i] == '0':
                closed_bracket+=1
            #When we cant make change 
            else:
                if s[i] == ')':
                    closed_bracket+=1
                    #Closed fixed bracket
                elif s[i] == '(':
                    opened_bracket+=1
                    #Opend fixed bracket
            #I have possiblity for making some opened bracker with 0
            closed_bracket+=allowed_to_change
            if opened_bracket > closed_bracket:
                #If the fixed closed bracket exceed we can not make a change 
                return False
           
        return True 
            
                
                
            
                   
        
        
        