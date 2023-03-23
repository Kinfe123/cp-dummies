class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result =[]
        def backtrack(curr , indx , t):
            if t == 0:
                result.append(curr[:])
          
                 
            if t <= 0:
                return 
            recently_used = -1
            for i in range(indx , len(candidates)):
                if recently_used == candidates[i]:
                    continue
                curr.append(candidates[i])
                backtrack(curr , i+1 , t-candidates[i])
                curr.pop()
                recently_used = candidates[i]
        backtrack([] , 0 , target)
        return result
            