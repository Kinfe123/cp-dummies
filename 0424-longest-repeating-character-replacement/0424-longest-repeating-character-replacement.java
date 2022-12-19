class Solution {
    public int characterReplacement(String s, int k) {
        // the key point here is keep track of the counter and slowing window
        // such that the difference between the window and counter should have to be 
        // less than or equal to the number of operation that we are allowed to make 
        
        
         int max_window = 0;
         HashSet<Character> Uniqueletters = new HashSet();
        for(int i=0; i<s.length(); i++){
            Uniqueletters.add(s.charAt(i));// we are collecting the unique charater 
        }
        for(Character eachLetter: Uniqueletters){
            int start = 0;
            
            int count = 0;
            for(int end=0; end<s.length(); end++){
                if(s.charAt(end) == eachLetter){
                    count++;
                }
                while(!isValidWindowSize(start , end , k , count)){
                    if(s.charAt(start) == eachLetter){
                        count--;
                        
                    }
                    start++; // for invalid window
                }
                max_window = Math.max(max_window , end-start+1);
            }
        }
        
        return max_window;
    
     
        
    }
    private Boolean isValidWindowSize(int start , int end , int k , int count){
        return end + 1 - start - count <= k;
    }
}