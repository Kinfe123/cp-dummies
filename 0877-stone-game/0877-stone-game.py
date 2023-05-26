class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l , r = 0 , len(piles)-1
        turn = 1
        alice , bob = 0, 0
        return True