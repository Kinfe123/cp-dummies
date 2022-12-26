
class Solution {
    public int longestSquareStreak(int[] nums) {
        Arrays.sort(nums);
        Map<Integer,Integer> mp = new HashMap<>();
        int ans = 0;
        for(int i:nums){
            int val = (int)Math.sqrt(i);

            if(val*val == i && mp.containsKey(val)){
                mp.put(i,mp.get(val)+1);
                ans = Math.max(ans,mp.get(i));
            }
            else mp.put(i,1);
        }
        return ans<2?-1:ans;
    }
}