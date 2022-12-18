class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        
        int r = arr.length-1;
        int l = 0;
        while(r - l >= k) {
            if(Math.abs(arr[l] - x) > Math.abs(arr[r] - x)){
                // we should have to shrink the distance - to make sure that we 
                // moving to the closest number we possibly could 
                l++;
            }else {
                r--;
            }
        }
        //after finding the right possible window for the value thought to be found
        // we can go over each and push them to Array
        List<Integer> output = new ArrayList<Integer>();
        for(int i = l; i<=r; i++){
            output.add(arr[i]);
        }
            
        return output;
    }
}