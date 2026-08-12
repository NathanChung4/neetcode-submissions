class Solution {
public:
    bool isAnagram(string s, string t) {
        // need 2 unordered_maps
        unordered_map<char, int> sMap;
        unordered_map<char, int> tMap;

        // loop through s
        for (int c : s) {
            sMap[c] += 1;
        }
        // loop through t
        for (int c : t) {
            tMap[c] += 1;
        }

        return sMap == tMap;
    }
};
