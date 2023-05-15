class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map_ = defaultdict(list)
        order =[]
        indeg = [0]*numCourses
        for c , p in prerequisites:
            map_[p].append(c)
            indeg[c]+=1
            
        q = deque()
        
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        while q:
            curr = q.popleft()
            order.append(curr)
            for nei in map_[curr]:
                indeg[nei]-=1
                if indeg[nei] == 0:
                    q.append(nei)
            
        return len(order) == numCourses
                
        
        