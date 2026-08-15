class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // need to return a list of lists
        vector<vector<int>> res;

        // need to sort nums
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            // check if the first pointer is a duplicate
            if (i > 0 && (nums[i] == nums[i-1])) {
                continue;
            }
            // left and right pointers
            int l = i+1;
            int r = nums.size()-1;

            while (l < r) {
                int three_sum = nums[i] + nums[l] + nums[r];

                if (three_sum > 0) {
                    r--;
                }
                else if (three_sum < 0) {
                    l++;
                }
                else {
                    res.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    while ((l < r) && (nums[l] == nums[l-1])) {
                        l++;
                    }
                }
            }
        }
        return res;
    }
};
