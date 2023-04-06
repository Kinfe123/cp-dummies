
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        #max lenght path could tell us the minumum number of nodes required to visit all
        reachable = [None] * n
        for i in edges:
            reachable[i[1]] = True
        result = [i for i in range(len(reachable)) if reachable[i] == None]
        return result 
        