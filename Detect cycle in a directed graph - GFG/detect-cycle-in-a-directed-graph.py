#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited = set()
        stack_tracker = [False] * V
        
        def dfs(node):
            #turn and them to our visited
            visited.add(node)
            stack_tracker[node] = True 
            for nei in adj[node]:
                if nei not in visited:
                    
                    if dfs(nei):
                        return True
                elif stack_tracker[nei]:
                  
                    return True 
            stack_tracker[node] = False
            return False
        for i in range(V):
            if i not in visited:
                if dfs(i):
                    return True 
                    
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends