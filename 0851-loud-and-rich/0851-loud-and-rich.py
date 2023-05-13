class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        def dfs(i):
            stack = [i]
            visited = set()
            more = float('inf')
            person = None
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    if quiet[node] <= more:
                        person = node
                        more = quiet[node]
                    for neighbour in adj[node]:
                        stack.append(neighbour)
            return person
        
        
        adj = defaultdict(list)
        for a, b in richer:
            adj[b].append(a)
        ans = [0 for i in range(len(quiet))]
        if richer:
            for i in range(len(quiet)):
                ans[i] = dfs(i)
        else:
            ans = sorted(quiet)
        return ans