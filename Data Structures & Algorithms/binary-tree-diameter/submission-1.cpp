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
private:
    int diameter = 0;
public:

    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);
        return diameter;
    }

    int dfs(TreeNode* root) {
        // base case
        if (!root) {
            return 0;
        }
        
        int leftDepth = dfs(root->left);
        int rightDepth = dfs(root->right);

        diameter = max(leftDepth + rightDepth, diameter);
        return max(leftDepth, rightDepth) + 1;
    }
};
