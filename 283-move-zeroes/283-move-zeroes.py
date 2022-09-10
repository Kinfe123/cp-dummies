class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = arr.count(0)
        for i in range(counter):
            arr.remove(0)
        for i in range(counter):
            arr.append(0)
        return arr