
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r=1,max(piles)
        while l<r:
            mid,t=(l+r)//2,0
            for i in piles: t+=math.ceil(i/mid)
           
            if t<=h:r=mid
            else:l=mid+1
        return l