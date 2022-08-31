class Solution:
    def firstUniqChar(self, s: str) -> int:
    
        if(len(s) != 0):
              hash_table = {}
              for char in s:
                  if char in hash_table:
                      hash_table[char] = hash_table[char] + 1
                  else:
                      hash_table[char] = 1

              for i, char in enumerate(s):
                  if hash_table[char] == 1:
                      return i

        return -1
        

        
        