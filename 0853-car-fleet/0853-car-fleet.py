class Solution: 
    def carFleet(self, target, position, speed):
            """
            :type target: int
            :type position: List[int]
            :type speed: List[int]
            :rtype: int
            """

            fleets = [[p , s] for p , s in zip(position,speed)]
            stack = []
            for p , s in sorted(fleets)[::-1]:
                stack.append((target-p)/s)
                if len(stack) >= 2  and stack[-1] <= stack[-2]:
                    stack.pop()
            return len(stack)
                
            