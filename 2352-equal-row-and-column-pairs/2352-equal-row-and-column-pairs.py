class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        map_ = Counter()
        counter = 0
        for i in grid:
            # o(MN) - since i am using a tuple for m row in n columns number 
            row = tuple(i)
            map_[row] += 1
        for i in range(len(grid)):
            temporary = []
            for j in range(len(grid[0])):
                temporary.append(grid[j][i])
        
            counter+=map_[tuple(temporary)]
        return counter 
            