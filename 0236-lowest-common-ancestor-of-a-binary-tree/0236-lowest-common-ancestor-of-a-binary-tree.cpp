/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == q || root == p){
             return root;
        }
        if(root == NULL){
            return NULL;
        }
        // }
        // TreeNode * left_sub = NULL;
        // TreeNode* right_sub = NULL;
        TreeNode* left_sub = lowestCommonAncestor(root->left , p , q);
        TreeNode* right_sub = lowestCommonAncestor(root->right , p , q);
    
     
        
        // cout << "THe nodes; " << left_sub << " - " << right_sub << endl;
        if(right_sub && left_sub ) {
            return root;
        }else if(left_sub != NULL && right_sub == NULL){
            return left_sub;
        }
        else if(left_sub == NULL && right_sub != NULL){
            return right_sub;
        }
        else{   
        return NULL;
        }
            
    
        
    }
};