from collections import defaultdict 
class Solution:
    def fib(self, n: int) -> int:
        map_ = defaultdict(int)


        def feb(x):
            if x == 1 or x == 0:
                return x

            else:
                if x not in map_:

                    map_[x] = feb(x-1) + feb(x-2)



                return map_[x]
        return feb(n)
    


       
        
        