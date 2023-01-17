from collections import *
from collections import Counter
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        

        
        rows , cols = len(matrix) , len(matrix[0])
        diagonal1 = defaultdict(list) 
        diagonal2 = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
               
                diagonal1[i-j].append(matrix[i][j])

        lists1 = []
        for keys, values in diagonal1.items():
            lists1.append(values)

        results = []
        for i in range(len(lists1)):
            first_element = lists1[i][0]
            if all(first_element == i for i in lists1[i]):
                results.append(True)
        if len(lists1) == len(results) and all(results):
            return True
        else:
            return False
