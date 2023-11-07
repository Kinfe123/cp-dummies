class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        res = -1
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                res = i
                break
        return res
        