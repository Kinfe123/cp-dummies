import itertools 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        new_list = []
        perm = itertools.permutations(nums)
        for i in perm:
            new_list.append(list(i))
        return new_list
        
        
        