class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        setA = set()
        pt1 = 'Not determined'
        pt2 = 'Not determined'
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if s[i] != goal[i]:
                if pt1 == "Not determined":
                    pt1 = i
                elif pt2 == "Not determined":
                    pt2 = i
                else:
                    return False # We have identified more two different points
                # so we can not perform any swapping
                
            setA.add(s[i])
        if pt1 != 'Not determined' and pt2 != 'Not determined':
            return s[pt1] == goal[pt2] and s[pt2] == goal[pt1]

        if pt1 != 'Not determined':
            return False
        # When both of are the same 
        return len(setA) < len(s)
            
            
        
            
        
        