class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Create a hash map that has key: value, value: index
        unordered_map<int,int> seen;

        // loop through the array and check if diff is in hashmap already
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (seen.find(diff) != seen.end()) {
                return {seen[diff], i};
            }
            seen[nums[i]] = i;
        }

    }
};
