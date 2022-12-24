class Solution:
    
    def sumOfNumbers(self , a1 , n):
        result = (n*(2*a1 + n - 1))//2
        return result 
        
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.insert(0 , 0)
        result = 0
        nums.append(2000000001)
       
        for i in range(len(nums)-1):
            starting = nums[i]
            ending = nums[i+1]
            if starting == ending:
                continue
            n = min(ending - starting - 1 , k )
            a = starting + 1
            '''
            we are trying to find the possible number that we could insert 
            which will be the min of the operation and range that we have 
            and try to add all those numebr as arth sum
            '''
            
            
            result += self.sumOfNumbers(a , n)
            k-=n
        return result 
        
            

        
