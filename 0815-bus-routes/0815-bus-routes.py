class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        map_ = defaultdict(set)
        seen = set()
        if source == target:
            return 0
        for bus_label , bus in enumerate(routes):
            for each_bus in bus:
                map_[each_bus].add(bus_label)
                

        seen = set()
        q = deque() 
        distance = 1
      
        for each in map_[source]:
            
            q.append(each)
            seen.add(each)
   
       
        while q:
            for _ in range(len(q)):
                
                idx = q.popleft()
             
                for bus_station in routes[idx]:
                    if bus_station == target:
                        return distance
                    for bus_s in map_[bus_station]:
                        if bus_s not in seen:
                            seen.add(bus_s)
                            q.append(bus_s)
                            
                        
                    
            
                
            
                        
                
            distance+=1
        return -1