class Solution:
    def pro(self , lists):
        product = 1
        for i in lists:
            product*=i
        return product
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        result =[]
        l , r = 0 ,  len(skill)-1
        summed = skill[l] + skill[r]
        while l < r:
            if skill[l] + skill[r] == summed:
                result.append([skill[l] , skill[r]])
                summed = skill[l] + skill[r]
                r-=1
                l+=1
            elif skill[l] + skill[r] > summed :
                r-=1
            elif skill[l] + skill[r] < summed:
                l+=1
        total = 0
        
        # print(result)
        if len(skill) == 2:
            return self.pro(skill)
        else:
            if len(result) == len(skill)//2:
                result = [i[0]*i[1] for i in result]
                return sum(result)
            else:
                return -1
            
            

            
        