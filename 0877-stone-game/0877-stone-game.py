class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l , r = 0 , len(piles)-1
        turn = 1
        alice , bob = 0, 0
        while l <=r:
            if turn % 2:
                
                if piles[l] >= piles[r]:
                    alice+=piles[l]
                    l+=1
                elif piles[l] < piles[r]:
                    alice+=piles[r]
                    r-=1
                # turn += 1
            else:
                if piles[l] >= piles[r]:
                    bob+=piles[l]
                    l+=1
                elif piles[l] < piles[r]:
                    bob+=piles[r]
                    r-=1
                # turn += 1
        return alice > bob 
                
                
