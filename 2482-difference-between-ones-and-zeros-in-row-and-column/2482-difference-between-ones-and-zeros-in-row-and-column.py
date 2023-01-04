class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row1, col1, row0, col0 = [], [], [], []
        m, n = len(grid), len(grid[0])

        for i in range(m):
            sums = 0
            for j in range(n):
                sums += grid[i][j]
            row1.append(sums)
            row0.append(n-sums)
            #Since n - sums represenr the remaining 0 which will be left off after
            #Substracting the lenght of sp. row with the summ of all of the 1 that we have
            #Found by far.

        for j in range(n):
            sums = 0
            for i in range(m):
                sums += grid[i][j]
            col1.append(sums)
            col0.append(m-sums)



        result = [[0 for _ in range(n)] for _ in  range(m)]

        for i in range(m):
            for j in range(n):
                result[i][j] = row1[i] + col1[j] - row0[i] - col0[j]
        return result 
