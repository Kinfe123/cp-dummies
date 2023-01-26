class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter = 0
        low , high = 0 , len(nums)-1
        while low < high:
            if nums[low] + nums[high] > k:
                high-=1
            elif nums[low] + nums[high] < k:
                low+=1
            else:
                counter+=1
                low+=1
                high-=1
                
        return counter 
            
        
        
        