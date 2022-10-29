class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        l = 0
        r = len(p)-1
        result = []
        while r < len(s):
            subs = Counter(s[l:r+1])
            if subs == counter:
                result.append(l)
            
            subs[s[l]] -= 1
            if subs[s[l]] == 0:
                subs.pop(s[l])
            l+=1
            r+=1
        return result
                
            