class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        max_ = 0
        lists = [i[0] for i in questions]
        for i in range(len(questions)-1 , -1 , -1):
            points , brainpower = questions[i]
            if i + brainpower+1 > len(questions)-1:
                max_ = max(max_ , lists[i])
            else:
                max_ = max(max_ , lists[i+brainpower+1] + lists[i])
                
            lists[i] = max_
            
        return lists[0]
                
#         n=len(questions)
#         l=[x[0] for x in questions]
#         maxi=0
#         for i in range(n-1,-1,-1):
#             if i+questions[i][1]+1>n-1:
#                 maxi=max(l[i],maxi)
#             else:
#                 maxi=max(l[i]+l[i+questions[i][1]+1],maxi)
#             l[i]=maxi
#         return l[0]