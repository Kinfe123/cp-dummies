class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        base_ = len(nums)/3
        lists = []
        for key , value in Counter(nums).items():
            if value > base_:
                lists.append(key)
        return lists 
                