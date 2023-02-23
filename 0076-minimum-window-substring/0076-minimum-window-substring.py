class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        found = 0
        counter_t = Counter(t)
        looking_for = len(counter_t)
        running_dict = defaultdict(int)
        pairs = (0 , 0)
        l , r = 0, 0
        result = 0 , 0
        min_ = float('inf')
        while r < len(s):
            running_dict[s[r]]+=1
            if s[r] in counter_t and running_dict[s[r]] == counter_t[s[r]]:
                found+=1
            while l <= r and looking_for == found:
                if r - l + 1 < min_:
                    pairs = l , r
                    min_ = min(min_ , r-l+1)
                running_dict[s[l]]-=1
                if running_dict[s[l]] == 0:
                    del running_dict[s[l]]
                if s[l] in counter_t and running_dict[s[l]] < counter_t[s[l]]:
                    # if it get affected by the deletion of the very first 
                    # element which makes the freq of the element to decrease  

                    found-=1
                l+=1
            r+=1
        return "" if min_ == float('inf') else s[pairs[0]:pairs[1]+1]
                