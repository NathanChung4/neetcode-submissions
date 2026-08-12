class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // need to return a list of lists
        map<vector<int>, vector<string>> res;

        for (string s : strs) {
            vector<int> count(26, 0);
            for (char c : s) {
                count[c - 'a']++;
            }
            res[count].push_back(s);
        }

        vector<vector<string>> output;

        for (auto& pair : res) {
            output.push_back(pair.second);
        }

        return output;


    }
};
