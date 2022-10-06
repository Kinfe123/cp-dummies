class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        #We can do it with a bruteforce approach - O(n^2) 
        #we can iterate each element in nested or 2d array
        #Bruteforce approach -
        #Time Comp = O(n^2)  and Space Comp = O(1) - constant space
        count = 0
        
        for i in grid:#traverse through the outer list
            for j in i:#For each element in the nested list
                if j < 0:
                    count+=1#keep counting when we get the number less than 0
        return count
        #The second approach we can use two pointer concept 
       
    
        