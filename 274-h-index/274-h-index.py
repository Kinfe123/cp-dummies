class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for indx , value in enumerate(citations):
            if indx >= value:
                return indx
        return len(citations)