
class Solution:
    
            
    def passThePillow(self, n: int, time: int) -> int:
        direction_change = -1
        pos = 0
        while time:
            if pos == n - 1 or pos == 0:
                direction_change*=-1
            pos+=direction_change
            time-=1
        return pos+1