class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        l = 0
        result = []
        nums.sort()
        i =0
        prefix_ = [0]
        max_ = float('-inf')
        for i in nums:
            prefix_ += [prefix_[-1] + i]
        for q in queries:
            for i in range(len(prefix_)):
                if q >= prefix_[i]:
                    max_ = max(max_ , i)
            result.append(max_)
            max_ = float('-inf')
        return result
            
            
            
            
  
                    
                    
            
        