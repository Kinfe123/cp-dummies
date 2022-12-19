class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        changed = str(x)[::-1]
    
        if str(x) == changed:
            return True
        else:
            return False
        