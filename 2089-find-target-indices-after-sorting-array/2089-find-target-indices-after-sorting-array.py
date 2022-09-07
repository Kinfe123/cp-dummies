class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lists = []
        for i in range(len(nums)):
            if nums[i] == target:
                lists.append(i)
            else:
                pass
        return lists if len(lists) > 0 else []
                
            
            
        