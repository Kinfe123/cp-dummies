class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrices = [[0] * numCourses for _ in range(numCourses)]
        #for making sure of the transitive property just using by the intermiediate vertext from the range(N)
        for u , v in prerequisites:
            matrices[u][v] = 1
        for inter in range(numCourses):
            for row in range(numCourses):
                for col in range(numCourses):
                    inter_ = matrices[row][inter] and matrices[inter][col]
                    matrices[row][col] = matrices[row][col] or (inter_)
                    
        return [matrices[a][b] for a , b in queries]
                    
                    
                    
       


        
        