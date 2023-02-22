class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        lenght = len(s1)
        running_dict = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            running_dict[s2[r]]+=1
            if r - l + 1 == lenght:
                if running_dict == counter:
                    return True 
                running_dict[s2[l]]-=1
                if running_dict[s2[l]] == 0:
                    del running_dict[s2[l]]
                l+=1
        return False
                
     