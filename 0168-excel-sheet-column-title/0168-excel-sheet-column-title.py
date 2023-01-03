class Solution:
    def convertToTitle(self, column: int) -> str:
        
        letter = [chr(c) for c in range(65 , 91)]
        output = ""

       
        leftOff = column - 1
        lists = []
        while leftOff >= 0:
            lists.append(letter[leftOff % 26])

            leftOff = leftOff // 26 - 1

        lists.reverse()
        result = "".join(lists)
        return result 
