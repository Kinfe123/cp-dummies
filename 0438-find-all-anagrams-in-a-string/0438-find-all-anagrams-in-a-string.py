class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        result = []
        running_dict = defaultdict(int)
        # r = len(p)-1
        for r in range(len(s)):
            running_dict[s[r]] += 1
            
            if r - l + 1 == len(p):
                
                if running_dict == Counter(p):
                    result.append(l)
                running_dict[s[l]]-=1
                if running_dict[s[l]] == 0:
                    del running_dict[s[l]]
                l+=1
        return result
                