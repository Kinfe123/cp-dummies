/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(!root){
            return res;
        }
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            vector<int> levels;
            int lenght = q.size();
            for(int i=0; i<lenght; i++){
                TreeNode *node = q.front();
                q.pop();
                levels.push_back(node->val);
                if(node && node->left){
                    q.push(node->left);
                    
                
                }
                if(node && node->right){
                    q.push(node->right);
                }
            }
            res.push_back(levels);
                
        
        
        }
      return res;
    }
};