class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lists = []
        l = [ 0 ] * 1001
        for numberOfPassenger , from_ , to in trips:
            
            lists.append([from_ , numberOfPassenger])
            lists.append([to , -numberOfPassenger])
            
        #To handle the passengers
        
        '''
        (1 , 2) , (5 , -2)  , (5 , 3) , (3 , 3) , (7 , -3) = 3
        
        
        '''
        lists.sort()
        p = 0
        for i in lists:
            p+=i[1]
            if p > capacity:
                return False
        return True
            
            