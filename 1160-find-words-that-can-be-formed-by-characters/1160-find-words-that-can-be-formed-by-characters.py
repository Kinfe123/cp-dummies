class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch = collections.Counter(chars)
        return sum(len(w) for w in words if collections.Counter(w) <= ch)
            
        