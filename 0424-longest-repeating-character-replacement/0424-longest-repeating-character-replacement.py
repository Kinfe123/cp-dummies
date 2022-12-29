class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_l = 0
        for i in range(ord('A') , ord('Z')+1):
            left = 0
            op = k
            target = chr(i)
            for right in range(len(s)):
                if s[right] != target:
                    op-=1
                while op < 0 and s[right]!=target:
                    if s[left]!=target:
                        op+=1
                    left+=1
                max_l = max(max_l , right-left+1)
        return max_l
        