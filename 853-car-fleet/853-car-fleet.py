class Solution: 
    def carFleet(self, target, position, speed):
            """
            :type target: int
            :type position: List[int]
            :type speed: List[int]
            :rtype: int
            """

            durations = [float(target - p ) / s for p, s in sorted(zip(position, speed))]

            res = 0
            prev = 0
            for d in durations[::-1]:

                if d <= prev:
                    continue

                res += 1
                prev = d
            return res