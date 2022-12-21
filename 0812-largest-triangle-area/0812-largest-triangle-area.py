class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        area = 0
        n = len(points)
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                for k in range(j+1,n):
                    x3,y3 = points[k]
                    curr = abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
                    if curr>area:
                        area = curr
        return area
#         area_max = 0
#         points.sort()
#         print(points
#              )
#         for i in range(len(points)-1 , 1 , -1):
#             pt1 , pt2 , pt3 = points[i] , points[i-1] , points[i-2]
#             print(pt3)
            
#             area = 0.5 * abs(pt1[0] * (pt2[1] - pt3[1]) + pt2[0] * (pt3[1] - pt1[1]) + pt3[0] *(pt1[1] - pt2[1]))
#             area_max = max(area_max , area)
            
#         return area_max
        
          
    
            
         