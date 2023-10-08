class Solution {
public:
    int f(int r , int c , vector<vector<int>> &dp , vector<vector<int>> &grid){
    if(r == 0 && c == 0){
        return grid[r][c];
    }
    if(r < 0 || c < 0){
        return INT_MAX;
    }
    if(dp[r][c] != -1){
        return dp[r][c];
    }
    
    int up = f(r-1 , c , dp , grid);
    int left = f(r , c -1 , dp , grid);

    dp[r][c] = min(up , left) + grid[r][c];
    return dp[r][c];
}

    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> dp(n , vector<int>(m , -1));
        return f(n-1 , m-1 , dp , grid);
        
    }
};