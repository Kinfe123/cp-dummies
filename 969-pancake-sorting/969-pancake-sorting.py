class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        op = []
        def flip(end):
            start = 0
            while start <= end:
                arr[start] , arr[end] = arr[end] , arr[start]
                start+=1
                end-=1
        for i in range(len(arr)-1 , -1 , -1):
            max_ = i
            for j in range(i , -1 , -1):
                if arr[max_] < arr[j]:
                    max_ = j
            if max_!=i:
                flip(max_)
                flip(i)
                op.append(max_+1)
                
                op.append(i+1)
        return op
                