class Solution {
    public int findClosestNumber(int[] nums) {
        int closerNumber = nums[0];
        List<Integer> ls = new ArrayList<Integer>();
        for(int i=0; i<nums.length; i++){
            if(Math.abs(nums[i]) < Math.abs(closerNumber)){
                closerNumber = (nums[i]);
            }
            if(Math.abs(nums[i]) == Math.abs(closerNumber)){
                if(nums[i] > closerNumber){
                    closerNumber = nums[i];
                }
            }
        }
        
        return  (closerNumber);
        
        
    }
}