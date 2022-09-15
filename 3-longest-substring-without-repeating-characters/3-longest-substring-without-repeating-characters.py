class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        uniqueChar = set()

        for right in range(len(s)):
            while s[right] in uniqueChar:
                uniqueChar.remove(s[left])
                left+=1
            uniqueChar.add(s[right])
            res = max(res , right-left+1)
        return res
                
        