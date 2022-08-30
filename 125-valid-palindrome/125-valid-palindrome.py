class Solution(object):
    def isPalindrome(self, word):
        
        word = word.lower()
        new_arr = []
        char = [":" , "," , "." , "@" , "#" , "_" , '.', "!" , "" ]
        if word == " ":
            return True
        else:
            for i in word:
                if i.isalnum():
                    new_arr.append(i)

        converted = "".join(new_arr) 
        reversedOne = []
        for i in range(len(converted)-1 , -1 , -1):
            reversedOne.append(converted[i])


        converted_1 = "".join(reversedOne)
        return converted_1 == converted
