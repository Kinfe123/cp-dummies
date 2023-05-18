import string

class unionFind:
        def __init__(self , size):
            self.size = size
            self.parent = [i for i in range(size)]
            self.rank = [1 for i in range(size)]

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
    def equationsPossible(self, equations: List[str]) -> bool:
        map_ = {i:i for i in string.ascii_lowercase}
        
        def find(vertice):
            if vertice != map_[vertice]:
                map_[vertice] = find(map_[vertice])
            return map_[vertice]
        def union(v1 , v2):
            map_[v1] = v2
        for each in equations:
            a_ , condition , b_ = each[0] , each[1] + each[2] , each[3]
            if condition == '==':
                r1 , r2 = find(a_), find(b_)
                union(r1 , r2)
                
        for each in equations:
            a_ , condition , b_ = each[0] , each[1] + each[2] , each[3]
            if find(a_) == find(b_) and condition == "!=":
                return False
        return True 
                    
                
                
        