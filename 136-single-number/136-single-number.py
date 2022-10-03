class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for key , value in Counter(nums).items():
            if value == 1:
                return key
                
            
                
            
                
        
                
                
        