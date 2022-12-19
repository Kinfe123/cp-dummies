class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        // int operation = k;
        // int right = 0;
        int longestOne = 0;
  
        int zeroCounter = 0;
        for(int right=0; right<nums.length; right++){
            if(nums[right]==0){
                zeroCounter++;
                
            }
            while(zeroCounter > k){
                if(nums[left] == 0){
                    zeroCounter--;
                    
                }
                left++;
                
                
                
                
            }
            longestOne = Math.max(longestOne , right-left+1);
            
        }
        return longestOne;
        
    }
}