
class Solution:
    
            
    def passThePillow(self, n: int, time: int) -> int:
        position = 1
        for i in range(time):
            if position == 1:
                change_dxn = 1
            elif position == n:
                change_dxn = -1
            print(position)
            position+=change_dxn
        return position