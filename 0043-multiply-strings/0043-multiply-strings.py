class Solution:
    def converter(self , number , n):
        num = 0
        n = len(number) 
        
        
      
        # Iterate till length of the string 
        for i in number: 

            # Subtract 48 from the current digit 
            num+=10**(n-1) * (ord(i) - 48)
            n-=1
    
        return num

       
            
        
        
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.converter(num1 , len(num1))*self.converter(num2  , len(num2)))        