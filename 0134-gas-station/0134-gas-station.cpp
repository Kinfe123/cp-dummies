class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int poss = 0;
        int poss_temp = 0;
        int idx  = 0;
        vector<int> d(gas.size() , 0);
        for(int i = 0; i < gas.size(); i++){
            int curr = gas[i] - cost[i];
            poss+=curr;
            poss_temp += curr;
            if(poss_temp < 0){
                poss_temp = 0;
                idx = i+1;
                
                
            }
            if(poss >= 0 && i == gas.size()-1){
                return idx;
            }
        }
        return -1;
        
    }
};