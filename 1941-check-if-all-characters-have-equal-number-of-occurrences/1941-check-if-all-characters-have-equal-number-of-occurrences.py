class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        words = Counter(s)
        list1 = list(words.values())
        first_one = list1[0]
        summed = sum(list1)
   
        if all(i == first_one for i in  list1):
            return True 
        return False
        