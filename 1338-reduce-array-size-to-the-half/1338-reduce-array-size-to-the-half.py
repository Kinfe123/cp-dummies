class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = Counter(arr)
        lists = []
        for keys , values in counter.items():
            lists.append(values)

        lists.sort()
        starter = 0
        counting = 0
        for i in range(len(lists)-1 , -1 , -1):
            starter += lists[i]
            counting+=1
            if starter >= len(arr)//2:
                break






        return counting 
