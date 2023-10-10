class Solution {
public:
    int maxSubarrays(vector<int>& nums) {
        if(nums.size() == 1){
            return 1;
        }
        int curr = nums[0];
        int n = nums.size();
        
        int target = nums[0];
        for(int i = 1; i<n; i++){
            target = target & nums[i];
        }
        
        int count = 1;
        // if(curr == 0){
        //     count += 1;
        // }
        for(int i=1; i<n; i++){
            if(curr == 0){
                count += 1;
                curr = nums[i];
            }else{
                curr &= nums[i];
            }
            // curr &= nums[i];
            // cout << "The current score: " << curr <<endl;
            
                
            }
        if(curr > 0 && count > 1){
            count--;
        }
        
            
    
        return count;
    }
};