class Solution {
public:
    int strStr(string haystack, string needle) {
        int indx = -1;
        int l = 0;
        int is_occured = false;
        
        while (l < haystack.size() ){
            bool isfound = true;
            int temp = l;
            for(int i=0; i<needle.size(); i++){
                
                if(haystack[temp] == needle[i]){
                temp+=1;
                }else{
                    isfound = false;
                    break;
                }
                
            }
            
            if(isfound){
                return l;
                
            }
            l+=1;
            
        }
        return -1;
        
    }
};