class Solution:
    def countPairs(self, nums: List[int]) -> int:
        # math.log2(4).is_integer() - for checking power of 2
        result = 0
        map_ = {}
        for num in nums:
            powerOf = 1
            for i in range(22):
                if powerOf-num in map_:
                    result += map_[powerOf-num]
                    result %= 10**9 + 7
                powerOf*=2
            if num not in map_:
                map_[num] = 1
            else:
                map_[num] += 1
        return result

            