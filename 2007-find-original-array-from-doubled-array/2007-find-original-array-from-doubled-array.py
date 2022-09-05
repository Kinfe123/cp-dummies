class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        n = len(changed)
        numF = Counter(changed)
        changed.sort()
        output = []
        if n % 2 != 0:
            return []
        for i in changed:
            if i == 0 and numF[i] >=2:
                numF[i] -= 2
                output.append(i)
            elif i > 0 and numF[i] and numF[i*2]:
                numF[i]-=1
                numF[i*2]-=1
                output.append(i)
        return output if len(output) == n / 2 else []
        