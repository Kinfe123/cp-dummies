class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        max_ = score = 0
        l , r = 0 , len(tokens)-1
        tokens.sort()
        while l <= r:
            if power >= tokens[l]:
                power-=tokens[l]
                score+=1
                max_ = max(score , max_)
                l+=1
            elif score > 0:
                power+=tokens[r]
                score-=1
                r-=1
            else:
                break
        return max_