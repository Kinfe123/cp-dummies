class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = []
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        # print(output)
        for char in s:
            if char == '#':
                digit1 = output.pop()
                digit2 = output.pop()
                output.append(digit2 * 10 + digit1)
            else:
                output.append(int(char))
        return "".join([alphabets[i-1] for i in output])