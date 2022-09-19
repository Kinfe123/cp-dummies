class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        starting_alt = 0
        max_ = min(gain)
        dummy = len(gain) + 1
        new_arr = [0] * dummy
        for i in range(0, len(gain)):

            starting_alt+=gain[i]
            new_arr[i] = starting_alt
        return max(new_arr)
        