class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l , r = 0 , len(piles)-1
        counter = 0
        while r>=l:
            r-=1
            counter+=piles[r]
            r-=1
            l+=1
        return counter
            