class Solution(object):
    def sortSentence(self, s):
        
       
       
        temp= s.split()
        word={}
        ans=''
        for i in temp:
            word[i[-1]]= i[:-1]
        for i in sorted(word):
            ans=ans+''.join(word[i])+' '
        ans=ans[:-1]



        return ans


text_1 = "is2 sentence4 This1 a3"
text_2 = "Myself2 Me1 I4 and3"
solution = Solution()
lists = solution.sortSentence(text_1)
lists_1 = solution.sortSentence(text_2)
sentence = " ".join(lists)
sentence_2 = " ".join(lists_1) 
print("\"{}\"".format(sentence))
print("\"{}\"".format(sentence_2))
