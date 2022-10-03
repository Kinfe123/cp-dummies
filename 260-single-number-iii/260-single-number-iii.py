class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lists = []
        for keys , values in Counter(nums).items():
            if values == 1:
                lists.append(keys)
        return lists
        