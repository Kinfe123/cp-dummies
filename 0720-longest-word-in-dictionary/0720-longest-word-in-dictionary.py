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
                return False , count
            curr = curr.children[word[i]]
            count +=1
        return True, count
    
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = Trie()
        res =[]
        for i in range(len(words)):
            curr = words[i]
            trie.insert(curr)
        
        map_ = defaultdict(int)
        best = ''
        max_l = float('-inf')
        for i in range(len(words)):
            curr = words[i]
            if len(curr) == 1 or curr[:len(curr)-1] in map_:
                map_[curr] = 1
                if len(curr) > len(best):
                    best = curr
                else:
                    continue
                res.append(curr)
            
        return best
            
    
        