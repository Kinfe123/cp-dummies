class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        lists = list(s)
        summed = sum(shifts)
        res = []
        for i in range(len(shifts)):
            res.append(summed)

            summed-=shifts[i]
      
        for i in range(len(res)):
            val = res[i] 
            ords = ord(lists[i]) - ord('a') # how far we are from 97 (a)
            result = ords + val # making a shift of character based on ascii
            result = result % 26 #we have to make it fall under the range of 26
            result+=ord('a') # now we can make it under the 97 ascii values
          
            lists[i] = chr(result)
        return "".join(lists)
        