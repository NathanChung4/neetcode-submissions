class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // need an unordered_set for o(1) lookup time
        unordered_set<int> newSet;

        for (int n : nums) {
            if (newSet.count(n)) {
                return true;
            }
            newSet.insert(n);
        }
        return false;
    }
};