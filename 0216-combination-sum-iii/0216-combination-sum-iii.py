class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        possible = [i for i in range(1 , 60)]
        res = []
        def back(i , summ , cand , c):
            if summ == n and  c == k:
                res.append(cand.copy())
                return
            if c == k or summ >= n:
                return 
            
            for i in range(i, 10):
                back(i+1 , summ + i , cand + [i], c+1)
                
                
            
        
        back(1 , 0 , [] , 0)
        # print(res)
        return res
        