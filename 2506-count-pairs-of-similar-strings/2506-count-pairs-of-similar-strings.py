class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # Counter()
        count = 0
        words = [set(i) for i in words]
        for i in range(len(words)-1):
            for j in range(i+1 , len(words)):
                if words[i] == words[j]:
                    count+=1
                    

        return count
        