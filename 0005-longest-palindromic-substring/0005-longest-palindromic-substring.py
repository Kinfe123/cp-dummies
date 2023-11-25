class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ''


        def findPalindrome(l, r):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l + 1 : r]

        for i in range(len(s)):
            # odd characters palindrome
            s1 = findPalindrome(i, i)
            # even characters palindrome
            s2 = findPalindrome(i, i + 1)

            #update resulte by comparing length of string
            if len(s1) > len(res):
                res = s1

            if len(s2) > len(res):
                res = s2

        return res
