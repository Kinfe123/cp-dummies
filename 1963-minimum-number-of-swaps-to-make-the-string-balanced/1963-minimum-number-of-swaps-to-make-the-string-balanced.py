class Solution:
    def minSwaps(self, s: str) -> int:
        balance , swap = 0 , 0
        for i in s:
            if i == "[":
                balance+=1
            else:
                balance -= 1
            if balance == -1:
                swap+=1
                balance = 1
        return swap

                