class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        max_ = 0
        uniqueChar = set()
        for r in range(len(s)):
            while s[r] in uniqueChar:
                uniqueChar.remove(s[l])
                l+=1
            uniqueChar.add(s[r])
            max_ = max(max_ , r-l+1)
        return max_
            
            
        