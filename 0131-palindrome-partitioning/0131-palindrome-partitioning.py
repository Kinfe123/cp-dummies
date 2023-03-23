class Solution:
    def ok(self , s , left, right):
        while left < right:
            if s[left] != s[right]:
            
                return False
            left+=1
            right-=1
        return True
    def partition(self, s: str) -> List[List[str]]:
        result , partitions = [] , []
        def backtrack(index):
            if index >= len(s):
                result.append(partitions[:])
                return 
            for i in range(index ,len(s)):
                if self.ok(s , index , i):
                    partitions.append(s[index:i+1])
                    backtrack(i+1)
                    partitions.pop()
        backtrack(0)
        return result