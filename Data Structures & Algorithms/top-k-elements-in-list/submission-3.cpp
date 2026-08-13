class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // need a hashmap to store frequencies
        unordered_map<int, int> counter;
        vector<int> res;

        // fill counter
        for (int n : nums) {
            counter[n] += 1;
        }

        // need a 2d array
        vector<vector<int>> newArray(nums.size()+1);

        // fill array
        for (auto& pair : counter) {
            newArray[pair.second].push_back(pair.first);
        }

        // loop through 2d array reversed until k is satisfied
        for (int i = newArray.size()-1; i > 0; i--) {
            for (int j = 0; j < newArray[i].size(); j++) {
                if (res.size() == k) {
                    return res;
                }
                res.push_back(newArray[i][j]);
            }
        }
        return res;
    }
};
