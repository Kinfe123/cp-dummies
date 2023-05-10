class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        coloring = [0 for _ in range(len(graph))]
        order = []
        def top_sort(node):
            if coloring[node] == 1:
                return False
            
            coloring[node] = 1
            for n in graph[node]:
                if coloring[n] == 2:
                #Cycle has been detected
                    continue
                if not top_sort(n):
                    return False
            
            coloring[node] = 2
            order.append(node)
            return True
        for i in range(len(graph)):
            if coloring[i] == 0:
                top_sort(i)
        return sorted(order)
                