
class Solution:           
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counter = 0
        l , r = 0 , len(people)-1
        people.sort()
        while l <= r:
            if people[l] + people[r] <= limit:
                r-=1
                l+=1
                #Both can taken since there weight is at most to the limit
              
            else:
                r-=1
                #It has to go alone since it is way to heavier for being taken by
                
                
            
            counter+=1
        return counter
        
        
        
                

        
       
        
        
        
        