class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        salary.pop(0)
        summed = sum(salary)
        return summed / len(salary)
            
        