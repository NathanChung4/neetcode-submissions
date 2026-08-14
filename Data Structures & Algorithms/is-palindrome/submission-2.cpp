class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.length() -1;

        while (l < r) {
            // advance pointers until valid chars
            while (l < r && isalnum(s[l]) == 0) {
                l++;
            }
            while (l < r && isalnum(s[r]) == 0) {
                r--;
            }

            // compare the pointers
            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }
            // advance the pointers
            l++;
            r--;
        }
        return true;
    }
};
