class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first_heavy = (heapq.heappop(stones))
            second_heavy = (heapq.heappop(stones))
            if second_heavy > first_heavy:
                heapq.heappush(stones , first_heavy - second_heavy  )
        stones.append(0)
        return abs(stones[0])
            