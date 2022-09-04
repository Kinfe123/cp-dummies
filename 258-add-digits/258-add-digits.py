class Solution(object):
    def add(self , n):
        conv = str(n)
        lists = [int(i) for i in conv]
        summed = sum(lists)
        return summed
    def addDigits(self, num):
        result = 0
        val = self.add(num)
        while not val < 10:
            val = self.add(val)
        if val < 10:
            result = val
        return result

        
        