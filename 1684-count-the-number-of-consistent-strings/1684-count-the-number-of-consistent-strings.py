class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        words = ["".join(sorted(set(i))) for i in words]
        count = 0
        allowed = sorted(allowed)
     
        for i in words:

            if all(c in allowed for c in i):
                count+=1
        return count
        