class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat) * len(mat[0]):
            return mat
        else:
            result = [[0] * c for _ in range(r)]
            lists = []
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    lists.append(mat[i][j])
            start = 0
            for i in range(len(result)):
                for j in range(len(result[0])):
                    if len(lists) != 0:
                        result[i][j] = lists[start]
                        start+=1
            return result 
                    
                    