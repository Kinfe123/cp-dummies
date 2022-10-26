class Solution:
#     def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
#         counter = 0
#         left , right = 0, k
#         while right <= len(arr):
            
#             subs = arr[left:right]
#             summed = sum(subs)
#             summed /= k
#             if summed >= threshold:
#                 counter+=1
#             left+=1
#             right+=1
        
        def numOfSubarrays(self, a: List[int], k: int, threshold: int) -> int:
            lo, sum_of_win, cnt, target = -1, 0, 0, k * threshold
            for hi, v in enumerate(a):
                sum_of_win += v
                if hi - lo == k:
                    if sum_of_win >= target:
                        cnt += 1
                    lo += 1   
                    sum_of_win -= a[lo]
            return cnt

            
            