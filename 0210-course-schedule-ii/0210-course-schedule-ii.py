class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        map_ = [[]  for _ in range(numCourses)]
        
        indegree = [0] * numCourses
        order = []
        q = deque()
        for a , b in prerequisites:
            map_[b].append(a)
            indegree[a] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            course = q.popleft()
            order.append(course)
            for child in map_[course]:
                indegree[child]-=1
                
                if indegree[child] == 0:
                    q.append(child)
        return [order , []][len(order) != numCourses]
        
            
               
            
            
        