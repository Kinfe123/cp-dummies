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
         // dp[i] = curr - dp[i-1] = prev
        vector<int> prev(m , 0);
        for(int i = 0; i < n; i++){
            vector<int> curr(m , 0);
            for(int j = 0; j<m; j++){
                if(obstacleGrid[i][j] == 1) curr[j] = 0;
                else if(i == 0 && j == 0) curr[j] = 1;
                else{
                int up = 0 , left =0 ;
                    if(i >0){
                        up = prev[j];
                    }if(j > 0){
                        left = curr[j-1];
                    }
                curr[j] = (up + left) % mod;
                }
                
            }
            prev = curr;
            

        }
        return prev[m-1];
        
    }
};