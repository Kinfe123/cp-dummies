class Solution {
public:
   int mod = (int)( 2 * 1e9 + 7);
long f(int r , int c , vector<vector<long>>&dp ,  vector<vector<int>> &mat){
    
    // if(mat[r][c] == -1) return 0;
    if(r >= 0 && c >= 0 && mat[r][c] ==  1) return 0; 
    
    if(r == 0 && c == 0) return 1;
    if(r < 0 || c < 0 ) return 0;
    if(dp[r][c] != -1) return dp[r][c];
    long long up = f(r - 1 , c , dp , mat);
    long long left = f(r , c - 1 , dp , mat);
    dp[r][c] = up + left;
    dp[r][c] %= mod;
    return dp[r][c];
    
}
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n = obstacleGrid.size();
        int m = obstacleGrid[0].size();
         
        vector<vector<long>> dp(n , vector<long>(m , -1));
    // dp[0][0] = 1;
    return f(n-1 , m-1 , dp , obstacleGrid) % mod;
        
    }
};