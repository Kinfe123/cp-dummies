class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        def backtrack(index , curr_comb , sum_):
            if sum_ >= target or index >= len(candidates):
                if sum_ == target:
                    result.append(curr_comb.copy())
                return 
            #including the unlimited the given number unlimited number of the 
            #time
            curr_comb.append(candidates[index])
            backtrack(index , curr_comb , sum_ + candidates[index])
            
            #NOt including the number but gonna be doing for including and not
            #not including for the not including itself
            elem = curr_comb.pop()
            
            backtrack(index+1 , curr_comb , sum_ )
            
        backtrack(0  , []  , 0)
        return result
            
            
        