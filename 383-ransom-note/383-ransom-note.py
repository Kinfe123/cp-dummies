class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine and ransomNote.count(i) <= magazine.count(i):
                pass
            else:
                return False
            
        return True