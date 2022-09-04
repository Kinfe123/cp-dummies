class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        for i in columnTitle:
            asci = ord(i) - ord('A') + 1
            res = res*26 + asci
            
            
        return res
        