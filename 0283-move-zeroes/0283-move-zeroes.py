class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counter = arr.count(0)
        # for i in range(counter):
        #     arr.remove(0)
        # for i in range(counter):
        #     arr.append(0)
        # return arr
        #track for the zeros to swap 
        finderForSwap = 0
        for nonZeroFinder in range(len(arr)):
            if arr[nonZeroFinder] != 0 and arr[finderForSwap] == 0:
                arr[nonZeroFinder] , arr[finderForSwap] = arr[finderForSwap] , arr[nonZeroFinder]
                
            if arr[finderForSwap] != 0:
                finderForSwap+=1
        return arr
                
            
            