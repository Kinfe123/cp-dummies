class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = "".join(sorted(s))
        str2 = "".join(sorted(t))
        if str1 == str2:
            return True
        return False