class Solution:
    def maxFinder(self , grid , i , j):
        max_ = 0
        for x in range(i , i+3):
            for y in range(j, j+3):
                max_ = max(max_ , grid[x][y])
        return max_
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0] * (n-2) for i in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                result[i][j] = self.maxFinder(grid , i , j)
        return result
        