class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        changed = str(x)[::-1]
        # arr = []
        # for i in range(len(changed)-1 , -1 ,-1):
        #     arr.append(changed[i])


        # converted = "".join(arr)
        # converted = int(converted)
        #it can be a changed variable here
        if str(x) == changed:
            return True
        else:
            return False
        