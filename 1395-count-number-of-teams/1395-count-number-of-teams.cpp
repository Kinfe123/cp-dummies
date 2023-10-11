class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        int count = 0;

        for(int i=0; i<n; i++) {

            int ls=0, ll=0, rs=0, rl=0;

            for(int l=i-1; l>=0; l--)  {
                if(rating[l]<rating[i])   {
                    ls++;
                }
                else {
                    ll++;
                }
            }

            for(int r=i+1; r<n; r++)  {
                if(rating[r]<rating[i])   {
                    rs++;
                }
                else {
                    rl++;
                }
            }


            count += (ls*rl) + (ll*rs);

            
        }

        return count;
    }
};