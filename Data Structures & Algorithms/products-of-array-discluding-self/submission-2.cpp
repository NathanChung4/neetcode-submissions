class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // need a result vector with same size as nums
        vector<int> res(nums.size());
        int prefix = 1;
        int postfix = 1;

        // first pass is prefix
        for (int i = 0; i < nums.size(); i++) {
            res[i] = prefix;
            prefix = prefix * nums[i];
        }
        // second pass is apply postfix (loop in reverse)
        for (int i = nums.size()-1; i > -1; i--) {
            res[i] = res[i] * postfix;
            postfix = postfix * nums[i];
        }

        return res;

    }
};
