class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lists = []
        op = k 
        number = max(arr)
        for i in range(1 , max(arr)+k+1):
            if i not in arr and op!=0:
                lists.append(i)
                op-=1
        return lists[-1]
            
        