class Solution:
    def numberOfWeakCharacters(self, number: List[List[int]]) -> int:
        sortedOne = sorted(number,key=lambda x: (x[0],-x[1])) 
        max_defense = 0
        counter = 0
        for i in range(len(sortedOne)-1 , -1 , -1):

            if sortedOne[i][1] < max_defense:
                counter+=1 
            else:
                max_defense = max(max_defense , sortedOne[i][1])
        return counter
        