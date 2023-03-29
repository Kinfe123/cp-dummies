class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        counter = Counter(nums)
        result = []
        counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1] , reverse=True)}
        result = list(counter)
        return result[:k]
            
        
        
        
            
        