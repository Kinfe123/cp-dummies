#include <vector>

class Solution {
public:
    int numTeams(std::vector<int>& rating) {
        int n = rating.size();
        std::vector<std::vector<int>> store(n, std::vector<int>(2, 0)); // Greater, Smaller
        int answer = 0;
        
        for (int i = 0; i < n; i++) {
            int right = rating[i];
            
            for (int j = i - 1; j >= 0; j--) {
                int left = rating[j];
                
                if (right > left) {
                    store[i][0] += 1;
                    answer += store[j][0];
                } else if (right < left) {
                    store[i][1] += 1;
                    answer += store[j][1];
                }
            }
        }
        
        return answer;
    }
};