class Solution:
    def maxArea(self, height: List[int]) -> int:
        low , high = 0 , len(height)-1
        max_ = float('-inf')
        while low <= high:
            area = (high-low) * min(height[low] , height[high])
            max_ = max(area , max_)
            if height[low] >= height[high]:
                high-=1
            elif height[low] < height[high]:
                low+=1
            
        return max_
            