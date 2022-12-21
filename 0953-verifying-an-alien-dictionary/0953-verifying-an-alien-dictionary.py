class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        dict_order = {char : indx for indx , char in enumerate(order)}
        for i in range(len(words)-1):
            word1 , word2 = words[i] , words[i+1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if dict_order[word1[j]] > dict_order[word2[j]]:
                        return False
                    break # we need to break since we on the order like eg1
        return True