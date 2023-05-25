class Solution:
    def canCompleteCircuit(self, gas: List[int], costs: List[int]) -> int:
      
        right_index = 0
        possible_count = 0
        reseted_count = 0
        for i in range(len(gas)):
            possible_count += gas[i]-costs[i]
            reseted_count += gas[i]-costs[i]
            if reseted_count < 0:
                reseted_count = 0
                right_index = i + 1
                
            if possible_count >= 0 and i == len(gas)-1:
                return right_index 
        return -1
              
            
            