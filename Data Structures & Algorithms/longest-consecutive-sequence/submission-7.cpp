class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // unordered_set
        unordered_set<int> newSet(nums.begin(), nums.end());
        int longest = 0;

        // loop through newSet
        for (int num: newSet) {

            // check if its first of sequence
            if (newSet.count(num - 1) == 0) {
                int currentNum = num;
                int current = 1;

                while (newSet.count(currentNum + 1)) {
                    currentNum++;
                    current++;
                }
                longest = max(current, longest);
            }
        }
        return longest;


    }
};
