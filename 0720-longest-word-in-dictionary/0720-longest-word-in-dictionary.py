class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self , word):
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
            
        curr.is_end = True
    def search(self , word):
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        return curr.is_end
    def pref(self , word):
        curr = self.root
        count =0
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False 
            curr = curr.children[word[i]]
            count +=1
        return True
    def pr(self , word):
        curr = self.root
        init = True
        for c in word:
            curr = curr.children[c]
            init = init and curr.is_end
            if not init:
                return False
        return True
    
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = Trie()
        res =[]
        best = ''
        for i in range(len(words)):
            curr = words[i]
            trie.insert(curr)
        for i in range(len(words)):
            curr = words[i]
            #Each of the word should have an end by them selves
            init = True
        
            # if
            
            # print('Curr , ' , curr , init)     
            if trie.pr(curr) and (len(curr) > len(best) or (len(curr) == len(best) and curr < best)):
                best = curr
        return best
       
            
    
        