class Solution:
    # def get_sum(self , range_sum , i , j):
    def longestWPI(self, hours: List[int]) -> int:
    
        dic = defaultdict(int)
        dummy = [1 if hours[0]>8 else -1]
        for h in hours[1:]:
            c = 1 if h>8 else -1
            dummy.append(dummy[-1]+c)

        res = 0
        for i in range(len(dummy)):
            if dummy[i]>0:
                res = max(res,i+1)
            else:
                if dummy[i]-1 in dic:
                    res = max(res,i-dic[dummy[i]-1])
                if dummy[i] not in dic:
                    dic[dummy[i]] = i

        return res
        
#     def longestWPI(self, hours: List[int]) -> int:
        
#         range_sum = [] * len(hours)
#         for i in range(len(hours)):
#             if i == 0:  
#                 if hours[i] > 8:
#                     range_sum[i] = 1
#                 range_sum[i] = -1
#             else:
#                 if hours[i] > 8:
#                     range_sum[i] = range_sum[i-1] + 1
#                 range_sum[i] = range_sum[i-1] - 1
        
#         output = 0
#         def get_sum(range_sum , i ,j):
    
#             if i > 0:
#                 left = range_sum[i-1]
#             else:
                
#                 left = 0
#             right = range_sum[j]
#             return right - left
#         for i in range(len(hours)):
#             for j in range(i , len(hours)):
#                 if get_sum(range_sum , i , j) > 0:
#                     output = max(output , j-i+1)
#         return output 

            


        