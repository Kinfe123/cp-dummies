class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # for i in range(num//2):
        #     for j in range(i+1 , num//2):
        #         for k in range(j+1 , num//2):
        #             if i + j + k == num and i == j-1 and j == k-1:
        #                 return [i , j , k]
#         for i in range(1 , num//2):
#             k = i + (i - 1) + (i+1)
#             if k == num:
#                 return [i-1 , i , i+1]
        
        if num % 3 == 0:
            
            result = [num//3-1  , num//3 , num//3+1 ]
        else:
            result = []
        return result 