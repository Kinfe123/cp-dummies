class unionFind:
        def __init__(self , size):
            self.size = size
            self.parent = [i for i in range(size+1)]
            self.rank = [1 for i in range(size+1)]

        def union(self , v1 , v2):
            r1 , r2 = self.find(v1) , self.find(v2)
        
            
            if self.rank[r1] > self.rank[r2]:
                self.parent[r2] = r1 
                self.rank[r2] = self.rank[r1]
            elif self.rank[r1] < self.rank[r2]:
                self.parent[r1] = r2
                self.rank[r1] = self.rank[r1]
            else:
                #both of the are equal and path has been compressed on the finding step which will add only 1 depth
                self.parent[r1] = r2
                #this means we are merging the r1 to r2 so r2 lenght will be incremented only by 1
                self.rank[r2]+=1

        def find(self , vertice):
            temp = self.parent[vertice]
            while temp != self.parent[temp]:
                temp = self.parent[temp]
            return temp
            # if self.parent[vertice] == vertice:
            #     return vertice
            # self.parent[vertice] = self.find(self.parent[vertice])

class Solution:
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        un = unionFind(len(edges))
        for u , v in edges:
            if un.find(u) == un.find(v):
                return [u , v]
            else:
                
                
                un.union(u , v)
    
                
                
                
                
        
        
        
        
        