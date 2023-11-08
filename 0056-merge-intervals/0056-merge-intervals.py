class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_one = sorted(intervals , key=lambda x:x[0])
        result = [sorted_one[0]]
        i = 1
        if len(sorted_one) == 1:
            return sorted_one
        else:
            while i < len(sorted_one):
                curr = sorted_one[i]
                if result[-1][1] >= curr[0]:
                    result[-1] = ([result[-1][0] , max(result[-1][1] , curr[1])])
                    i+=1
                else:
                   
                    result.append(curr)
                    i+=1

            # print(i)
            return result 
        