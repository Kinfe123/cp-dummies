class Solution:
    def longestOnes(self, nums: List[int], k: int , target: str) -> int:
        max_ = 0
        start = 0
        targetCount = 0
        for end in range(len(nums)):
            if nums[end] == target:
                targetCount+=1
            while targetCount > k:
                if nums[start] == target:
                    targetCount-=1
                start+=1
            max_= max(max_ , end-start+1)
        return max_
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        return max(self.longestOnes(answerKey , k , 'T'), self.longestOnes(answerKey , k , 'F'))
    
                