class Solution {
public:
    
    int count(int r , int c , vector<vector<int>>&dp){
        if(dp[r][c] != -1) return dp[r][c];
        
        if(r == 0 || c == 0) return 1;
        if(r < 0 || c < 0) return 0;
        int up = count(r-1 ,c , dp);
        int left = count(r , c-1 , dp);
        dp[r][c]= up + left;
        return dp[r][c] ;
    }
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m , vector<int>(n , -1));
        // dp[0][0] = 1;
        return count(m -1, n-1 , dp);
//         for(int i=1; i<m; i++){
//             for(int j = 1; j<n; j++){
//                 dp[i][j] = dp[i-1][j] + dp[i][j-1];
//             }
//         }
        
//         for(int i=0; i<m; i++){
//             for(int j=0; j<n; j++){
//                 cout<< "The values are: " << dp[i][j] << endl;
//             }
//         }
        // return dp[m-1][n-1];
        
    }
};