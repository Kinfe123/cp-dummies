class Solution(object):
    def kClosest(self, points, k):
        points = sorted(points, key = lambda x:math.sqrt(pow(x[0] , 2) + pow(x[1] , 2)))
        return points[:k]
 

solution = Solution()
print(solution.kClosest([[1,3],[-2,2]] , 1))