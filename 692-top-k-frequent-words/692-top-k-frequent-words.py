class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        new_arr = []
        for i in words:
            if i not in new_arr:
                new_arr.append(i)

        for i in new_arr:
            dic[i] = words.count(i)
        sorted_tuples = sorted(dic.items()  , key=operator.itemgetter(1) , reverse=True)
        op = []
        sorted_tuples.sort(key=lambda x:(-x[1], x[0]))
        for i in range(k):
            op.append(sorted_tuples[i][0])
        return op
            