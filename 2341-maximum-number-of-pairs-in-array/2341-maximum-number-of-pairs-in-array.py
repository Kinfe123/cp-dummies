class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        pair = 0
        lety = 0
        for i in s.keys():
            pair+=s[i]//2
            lety+=s[i]%2
        return [pair , lety]
        #1:2 , 3:2 , 2:3 pair = pair + s[1]