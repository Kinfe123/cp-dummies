class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.replace("i" , "j")
        num2 = num2.replace("i" , "j")

        c1 = num1.split("+")
        c2 = num2.split("+")
        result = []
        for i in range(len(c1)):
            for j in range(len(c2)):

                result.append([c1[i] , c2[j]])

        final = 0
        for pairs in result:
            x , y = pairs[0] , pairs[1]
            final+= complex(x) * complex(y)



        an = ""


        imag = int(final.imag)
        real = int(final.real)

        an = f"{real}+{imag}i"
        
        return an

