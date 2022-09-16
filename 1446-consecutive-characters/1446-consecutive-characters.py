class Solution:
     def maxPower(self, s: str) -> int:
        cnt = ans = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1
        return ans