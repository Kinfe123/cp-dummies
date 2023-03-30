class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lists  = [i for i in range(1 , len(nums)+1)]
        result = []
        counter = Counter(nums)
        result.append(list(set(lists).difference(set(nums))))
        result.append(list(keys for keys , values in counter.items() if values == 2))
    
        return [result[1][0] , result[0][0]]
#         nums.sort()
#         result = [0] * 2
#         i = 0
#         for i in range(len(nums)):
#             if nums[i] ^ lists[i]:
                
#                 result[i]  = nums[i] ^ lists[i]
#                 i+=1
            
                
#         return result 
                
                