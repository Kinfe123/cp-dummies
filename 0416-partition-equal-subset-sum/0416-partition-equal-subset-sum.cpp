class Solution {
public:
    
int f(int idx  , int target , vector<int> &arr,  vector<vector<int>> &dp){
    if(idx < 0){
        return false;
    }
    if(idx == 0) {
        if(arr[idx] == target){
            return true;
        }
    }
    if(target == 0) return true;
    if(dp[idx][target] != -1) return dp[idx][target];
    bool notTake = f(idx -1 , target ,arr , dp);
    bool take = false;
    if(target >= arr[idx]) {
         take = f(idx-1 , target - arr[idx] , arr , dp);

    }
    dp[idx][target] = take || notTake;

    return dp[idx][target];
}
    bool canPartition(vector<int>& nums) {
        int summ = 0;
        for(int i=0; i<nums.size(); i++) summ+=nums[i];
        // cout << "THe sum : " << summ <<endl;
        vector<vector<int>> dp(nums.size() + 1 , vector<int>(summ+1 , -1));
        if(summ % 2 == 1){
            return false;
        }else {
            
            return f(nums.size()-1 , summ/2 , nums , dp);
        }
        
    }
};