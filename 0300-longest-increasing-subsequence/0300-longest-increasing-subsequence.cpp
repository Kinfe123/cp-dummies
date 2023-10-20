class Solution {
public:
    int count(int idx , vector<int>&nums){
     if(idx == nums.size()) return 1;
     int curr = 1;
      for(int i=idx-1; i>=0; i++){
          if(nums[idx] < nums[i]){
              curr = max(curr , 1 + count(i , nums));
          }
      }
    return curr;
        
    }

    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n , 1);
        for(int i = 0; i<n; i++){
            for(int j = i; j < n; j++){
                if(nums[i] < nums[j]) dp[j] = max(dp[j] , 1+dp[i]);
                
            }
        }
        // cout << d
        // return count(0 , nums);
        int max_ = dp[n-1];
        return max(max_ , *max_element(dp.begin() , dp.end()));
        
    }
};