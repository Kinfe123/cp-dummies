class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        res = -1
        for i in range(len(s)):
            if c[s[i]] == 1:
                res = i
                break
        return res
        