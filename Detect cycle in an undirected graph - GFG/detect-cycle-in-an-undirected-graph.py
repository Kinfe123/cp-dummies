from typing import List
from collections import defaultdict
class Solution:
    
    '''
    result = [set() for _ in range(n)]
        graph = defaultdict(list)
        glo_visited = set()
    '''
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    map_ = defaultdict(list)
	    visited = set()
	    def dfs(source , i):
	        
	        
	        visited.add(i)
	        for nei in adj[i]:
	            if nei not in visited:
	                if dfs(i , nei):
	                    return True
	            elif source != nei:
	                return True 
	                
	        return False
	        
	        
	        
	        
	    for i in range(V):
	       # visited = set()
	        if i not in visited:
    	        if dfs(-1 , i):
    	            return True 
	    return False
	        
	        
		#Code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends