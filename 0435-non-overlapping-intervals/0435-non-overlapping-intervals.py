class Solution:
    def eraseOverlapIntervals(self, interval: List[List[int]]) -> int:
        interval.sort()
        prev_end = interval[0][1]
        out = 0
        for start , end in interval[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                out+=1
                prev_end = min(end , prev_end)
        return out 