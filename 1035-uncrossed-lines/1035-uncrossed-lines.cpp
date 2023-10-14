class Solution {
public:
//     int dp(int i , int j  , vector<int>&dp , vector<int> &nums1 , vector<int>&nums2){
        
//         if(i == nums1.size() || j == nums2.size()){
//             return 0;
//         }
//         int res = max(f(i+1, j , dp , nums1 , nums2) , f(i , j+1  dp , nums1 , nums2));
//         if(nums1[i] == nums2[j]){
//             res = max(res , f(i+1 , j+1 , dp , nums1 , nums2));
//         }
//         return nums;
//     }
    int maxUncrossedLines(vector<int>& text1, vector<int>& text2) {
        int n = text1.size();
        int m = text2.size();
        // int dp[n+1][m+1];
        vector<vector<int>> dp(n+1 , vector<int>(m+1 , 0));
        int res = 0;
        // memset(dp, 0, sizeof(dp));
        for(int i =1; i<=n; i++){
            for(int j = 1; j <= m; j++){
                if(text1[i-1] == text2[j-1]){
                    dp[i][j] = dp[i-1][j-1] + 1;
                    res = max(res , dp[i][j]);
                    
                }
                else {
                    // at some point we might have passed by the string that have the same val
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1] );
                }
            }
        }
       
        return res;
    }
};