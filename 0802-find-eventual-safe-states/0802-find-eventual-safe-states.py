class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        coloring = [0 for _ in range(len(graph))]
        order = []
        def top_sort(node):
            #Cycle has been detected and we can not move anyfar.
            if coloring[node] == 1:
                return False
            
            coloring[node] = 1
            for n in graph[node]:
                if coloring[n] == 2:
                    #Processed before 
                    continue
                if not top_sort(n):
                    return False
            
            coloring[node] = 2
            #Marking it as processed since it wil be leading us to terminal node 
        
            order.append(node)
            
            return True
        for i in range(len(graph)):
            if coloring[i] == 0:
                top_sort(i)
        return sorted(order)
                