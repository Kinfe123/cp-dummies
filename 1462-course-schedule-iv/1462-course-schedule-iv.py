class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        map_ = defaultdict(list)
        process = defaultdict(set)
        indeg = [0] * numCourses
        for pre , course in prerequisites:
            map_[pre].append(course)
            indeg[course] += 1
            
        q = deque()
        for i in range(numCourses):
            if not indeg[i]:
                q.append(i)
                
        
        
        while q:
            curr = q.popleft()
            #we have found the one who has not any kind of prerequistes so lets find out for whom it can be a prerequisites
            for nei in map_[curr]:
                #here we will be doing somekind of transitivity
                process[nei].add(curr)
                process[nei].update(process[curr])
                indeg[nei]-=1
                if not indeg[nei]:
                    q.append(nei)
                    
        return [u in process[v] for u , v in queries]

                    
        
                    
                    
                    
       


        
        