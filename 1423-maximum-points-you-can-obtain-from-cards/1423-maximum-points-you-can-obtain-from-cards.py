class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left , right = 0 , len(cardPoints)-k
        summed = sum(cardPoints[right:])
        result = summed
        while right < len(cardPoints):
            summed += (cardPoints[left] - cardPoints[right])
            #Removing the right one and adding the left one 
            result = max(result , summed)
            left+=1
            right+=1
        
            
        return result
            
            