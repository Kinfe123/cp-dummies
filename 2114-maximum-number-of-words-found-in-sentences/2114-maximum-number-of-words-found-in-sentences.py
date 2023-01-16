class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        lists = [i.split() for i in sentences ]
        lists = [len(i) for i in lists]
        return max(lists)
        