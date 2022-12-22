class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_list = set([i[0] for i in matches])
        losser_list = set([i[1] for i in matches])
        lossing_dict = {}
        output_win = []
        output_one_win = []
        for win , loss in matches:
            if loss in lossing_dict:
                lossing_dict[loss] += 1
            else:
                lossing_dict[loss] = 1
        for i in winner_list:
            if i not in lossing_dict:
                output_win.append(i)
            
        for i in losser_list:
            if lossing_dict[i] == 1:
                output_one_win.append(i)
                
                
        # print(lossing_dict)
        # print(winner_list)
        output_win.sort()
        output_one_win.sort()
        return [output_win , output_one_win]
                
            
        