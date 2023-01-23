class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        max_ = 0
        piles.sort()
        next_max= [0] * (len(piles)//3)
        ind = len(piles)-2
        j = 0
        while j < len(next_max):
            next_max[j] = piles[ind]
            ind-=2
            j+=1
        return sum(next_max)
        