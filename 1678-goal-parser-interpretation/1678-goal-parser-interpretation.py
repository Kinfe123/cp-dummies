class Solution:
    def interpret(self, command: str) -> str:
        string_for = [ ]
        dict_ = {"G" : "G" , "()" :'o' , "(al)": 'al'}
        
        for i in range(len(command)):
            if command[i] == "G":
                string_for.append("G")
            elif command[i] == '(':
                string_for.append('o' if command[i+1] == ")" else "al")
            
            
            
        return "".join(string_for)
        
        