class Solution:
    def removeDuplicateLetters(self, letter: str) -> str:
        lookingup = {}
        for i in range(len(letter)):
            lookingup[letter[i]] = i # This keep track of the very last occurance of the letters
            
        stack = []
        looked_up = set()
        for i in range(len(letter)):
            if letter[i] in looked_up:
                continue
            while stack and stack[-1] > letter[i] and lookingup[stack[-1]] > i:
                looked_up.remove(stack[-1])
                stack.pop()
            stack.append(letter[i])
            looked_up.add(letter[i])
        return "".join(stack)