class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        possibles = [i for i in range(0 , int(sqrt(c))+1)]
    
        low , high = 0 , len(possibles)-1
        while low <= high:
         
            if possibles[low] ** 2 + possibles[high] ** 2 > c:
                high-=1
            elif possibles[low] ** 2 + possibles[high]**2 < c:
                low+=1
            else:
                return True
        return False
        

        # print(possibles)
                
            