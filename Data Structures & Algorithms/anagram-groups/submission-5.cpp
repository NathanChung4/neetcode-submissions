class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        // create the dictionary
        unordered_map<string, vector<string>> mp;

        // loop through the list of strings
        for (const auto& s : strs) {
            vector<int> count(26, 0);

            for (char c : s) {
                count[c - 'a']++;
            }
            string key = to_string(count[0]);
            for (int i = 1; i < 26; i++) {
                key += ',' + to_string(count[i]);
            }
            mp[key].push_back(s);
        }
        vector<vector<string>> result;
        for (const auto& pair : mp) {
            result.push_back(pair.second);
        }
        return result;

    }
};
