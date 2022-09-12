class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}  # map
        s = 0
        cnt = 0
        for v in nums:
            s += v
            if s - k in d:
                  cnt += d[s-k]
            d[s] = d.get(s, 0) + 1
        return cnt
