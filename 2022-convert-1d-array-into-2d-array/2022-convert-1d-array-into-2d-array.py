class Solution:
    def construct2DArray(self, original: List[int], r: int, c: int) -> List[List[int]]:
        lists = original
        if len(lists) != r*c:
            return []
        else:

            result = [[0] * c for _ in range(r)]
            start = 0
            for i in range(len(result)):
                for j in range(len(result[0])):
                    if len(lists) != 0:
                        result[i][j] = lists[start]
                        start+=1
            return result 