class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]
        for starting , ending in intervals[1:]:
            veryLstEnd = res[-1][1]
            if starting <= veryLstEnd:
                res[-1][1] = max(veryLstEnd , ending)
            else:
                res.append([starting , ending ])

        return res
        