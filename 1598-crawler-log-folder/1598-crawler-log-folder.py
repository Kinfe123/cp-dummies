class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for i in logs:
            if i == "./":
                continue
            elif i == "../":
                if result > 0:
                    result -= 1
            else:
                result+=1
        return result 