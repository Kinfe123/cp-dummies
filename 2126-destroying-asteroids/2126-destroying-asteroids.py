class Solution:
    def asteroidsDestroyed(self, mass: int, nums: List[int]) -> bool:
        masses = mass
        nums.sort()
        flag = []
        for i in range(len(nums)):
            if masses >= nums[i]:
                masses+=nums[i]
                flag.append(True)
            else:
                flag.append(False)

        return all(flag)
        