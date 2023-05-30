class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        count = 0
        
        def find(index , count):
            if index == len(nums):
                if count == target:
                    return 1
                return 0
          
            if (count , index) in dp:
                return dp[(count , index)]
            add_way = find(index+1 , count + nums[index])
            minus_way = find(index+1 , count - nums[index])
            dp[(count , index)] = add_way + minus_way 
            return dp[(count , index)]
                
                
        val = find(0 , 0)
        return val
                
                
            

        
        