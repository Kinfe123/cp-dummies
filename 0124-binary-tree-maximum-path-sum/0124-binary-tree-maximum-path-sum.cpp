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
    
    // int res=0;
    int collect(TreeNode *node , int &res){
        if(!node){
            return 0;
        }
        if(!node->left && !node->right){
            res = max(res , node->val);
            return node->val;
        }
        int left = max(collect(node->left , res) , 0);
        int right = max(collect(node->right , res) ,0);
        res = max(res , (node->val + left + right));
        return max(left , right) + node->val;
    }
public:
    int maxPathSum(TreeNode* root) {
        // int res = root->val
        int res = INT_MIN;
        // vector<vector<int>> dp()
        collect(root , res);
        return res;
        
    }
};