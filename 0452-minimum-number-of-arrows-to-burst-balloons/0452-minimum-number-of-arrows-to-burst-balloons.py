class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        min_= 1
        # the one with the first would be the one who get brusted , then we will be brust
        end = points[0][1]
        for i in range(1 , len(points)):
            start_ , end_ = points[i]
            if start_ > end:
                min_+=1
                end = end_
            else:
                #the edge case that got have to handle - which one might engulf the other two that aint overlaps
                end = min(end , end_)
                
                
            
     
        return min_