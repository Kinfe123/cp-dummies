class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        final_result = [ ]
        notFound = set()
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        row = 0 
        
        for i in range(len(words)):
            isExist = True
            wordToCheck = words[i]
            rowDeterminer = words[i][0]
            rowDeterminer = rowDeterminer.lower()
            if rowDeterminer in first_row:
                row = first_row
            elif rowDeterminer in second_row:
                row = second_row
            else:
                row = third_row
            # print(row)
            for char in range(1 , len(wordToCheck)):
                while wordToCheck[char].lower() not in row :
                    isExist = False
                    notFound.add(wordToCheck)
                    break
                
                # if isExist == True:
                #     another_list.append(wordToCheck)
        for i in words:
            if i not in notFound:
                final_result.append(i)
                
        return final_result
        
                    
                    