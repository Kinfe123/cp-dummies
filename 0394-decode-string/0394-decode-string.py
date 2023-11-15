class Solution:
    def decodeString(self, s: str) -> str:
        decode = []
        cummulate_string = ""
        k = 0
        for i in range(len(s)):
            curr = s[i]
            #open bracket means 
            if curr == '[':
                temp = (cummulate_string , k)
                decode.append(temp)
                k = 0
                cummulate_string = ""
                
                
            
            
            #closing bracket means we have to pop from the top of the stack
            #and propagate the commulate_string
            elif curr == ']':
                latest_string , latest_k = decode.pop()
                to_append = latest_k * cummulate_string
                # print('curr: ', to_append , cummulate_string)
                cummulate_string = (latest_string + to_append)
                
                
            elif curr.isalpha():
                cummulate_string+=curr
            elif curr.isdigit():
                #update k 
                k = k * 10 + int(curr)
            else:
                pass
        return cummulate_string
            
                