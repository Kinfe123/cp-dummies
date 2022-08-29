import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}
        new_arr = []
        for i in nums:
            if i not in new_arr:
                new_arr.append(i)

        for i in new_arr:
            dic[i] = nums.count(i)
        sorted_tuples = sorted(dic.items() , key=operator.itemgetter(1) , reverse=True)
        op = []
        for i in range(k):
            op.append(sorted_tuples[i][0])
        return op
            
        