class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_ = float('-inf')
        l = 0
        fruit_map = defaultdict(int)
        for r in range(len(fruits)):
            fruit_map[fruits[r]]+=1
            
            while len(fruit_map) > 2:
                fruit_map[fruits[l]]-=1
                if fruit_map[fruits[l]] == 0:
                    del fruit_map[fruits[l]]
                l+=1
            max_ = max(r - l + 1 , max_)
        return max_

        
        
   
    
        