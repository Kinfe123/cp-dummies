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
    int moves =0;
    int dfs(TreeNode *root){
        if(root == NULL) return 0;
        int l = dfs(root->left);
        int r = dfs(root->right);
        
        moves += (abs(l) + abs(r));
        // putting on extra for it self and sending the rest of coins
        
        return (l + r + root->val - 1);
    }
    int distributeCoins(TreeNode* root) {
        dfs(root);
        return abs(moves);
        
    }
};