class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
    
        self.counter = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        self.counter[self.nums2[index]]-=1
        
        self.nums2[index] += val
        self.counter[self.nums2[index]]+=1
    def count(self, tot: int) -> int:
        temp = 0
        for i in self.nums1:
            temp+=self.counter[tot-i]
        return temp
        # sets = set(self.counter.keys())
        # self.counter = Counter(self.nums1)
        # for i in range(len(self.nums2)):
        #     rem = tot-self.nums2[i]
        #     if rem in sets:
        #         temp += self.counter[rem]
        # return temp
        
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)