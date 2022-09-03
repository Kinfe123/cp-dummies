class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums = ""
        for i in digits:
            nums+=str(i)
        nums_converted = int(nums) + 1
        nums_converted = str(nums_converted)
        new_list = []
        for i in nums_converted:
            new_list.append(i)
        return new_list
            
        
        
        