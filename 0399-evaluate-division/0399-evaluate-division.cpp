class Solution {
    void dfs(string& s,string& d,unordered_map<string,vector<pair<string,double>>>& g,set<string>& vis, double& ans, double temp)
    {
        if(vis.find(s) != vis.end()){ 
            return;
        }else{
            vis.insert(s);
            if(s==d){   
                ans = temp;
                return;
            }else{
                for(auto adj : g[s]){ 
                    dfs(adj.first,d,g,vis,ans,temp*adj.second);
                }
            }
        }

    }

public:
    vector<double> calcEquation(vector<vector<string>>& e, vector<double>& v, vector<vector<string>>& q) {
     
        unordered_map<string,vector<pair<string,double>>> g;
        for(int i = 0; i < e.size(); i++){
            string n = e[i][0];
            string d = e[i][1];
            double val = v[i];
            g[n].push_back({d,val}); 
            g[d].push_back({n,1/val}); 
        }
       
        vector<double> res;
        for(int i = 0; i < q.size(); i++){
            string s = q[i][0];
            string d = q[i][1];
            set<string> vis;
            double ans = -1.0;
            if(g.find(s) != g.end()) 
                dfs(s,d,g,vis,ans,1.0);
            res.push_back(ans);
        }
        return res;
    }
};