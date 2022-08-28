import math
class Solution(object):
    def isPerfectSquare(self, num):
        result = num**0.5
        if result == math.ceil(result):
            return True
        return False
