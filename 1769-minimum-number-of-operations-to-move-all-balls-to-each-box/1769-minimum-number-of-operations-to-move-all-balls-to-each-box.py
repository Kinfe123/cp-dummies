class Solution:
    
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        n = len(boxes)
        for i in range(n):

            total = 0
            for left in range(i - 1 , -1 , -1):
                if boxes[left] == "1":
                    total+= i - left
            for right in range(i+1 , n):
                if boxes[right] == "1":
                    total+= right - i
            result.append(total)
        return result 
