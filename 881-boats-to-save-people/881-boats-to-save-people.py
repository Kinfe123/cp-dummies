class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left , right = 0 , len(people) - 1
        people.sort()
        result = 0
        while left <= right:
            mod = limit - people[right]
            result+=1
            right-=1
            if left<=right and mod >= people[left]:
                left+=1
        return result             
            
        